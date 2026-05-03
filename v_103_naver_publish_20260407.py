"""
네이버 블로그 자동발행 스크립트
==================================================
버전: v.103 (2026-04-07)
구조: 작업폴더/input/ 에 JSON 설계도 + 이미지 전부 넣고 실행

변경 이력:
  v.102 → v.103
    - undetected_chromedriver + pyperclip 자동 로그인 (v.211 검증 방식)
    - 신/구 에디터 자동 감지 (iframe 유무)
    - 드라이버 시작 속도 개선 (패치 캐시 재사용)
    - 캡션 입력 개선 (WebDriverWait + JS 클릭 폴백)
    - 오버레이 자동 제거

사용법:
  1. input/ 폴더에 naver_*.json + 이미지 파일들 넣기
  2. 아래 계정 설정 확인
  3. python v_103_naver_publish_20260407.py
  4. 자동 로그인 → 글쓰기 페이지 이동
  5. 알림창 수동 닫기 → F8 → 자동 입력
  6. 완료 후 미리보기 확인 → 카테고리 선택 → 발행

필수 패키지:
  pip install selenium undetected-chromedriver pyperclip keyboard
"""

import json
import os
from dotenv import load_dotenv

load_dotenv()

# ═══════════════════════════════════════════════════════════
# 🔥 하드코딩 설정 - 여기만 수정하세요!
# ═══════════════════════════════════════════════════════════

# ===== 계정 설정 =====
AUTO_LOGIN_ID = os.getenv("NAVER_ID")
AUTO_LOGIN_PW = os.getenv("NAVER_PW")

if not AUTO_LOGIN_ID or not AUTO_LOGIN_PW:
    print("❌ .env 파일에서 NAVER_ID/NAVER_PW를 찾을 수 없습니다.")
    print("   📁 C:\\Claude_Code\\blog\\.env 파일을 확인하세요.")
    print("   📋 Google Drive 비공개 문서에 백업본이 있을 거예요.")
    import sys
    sys.exit(1)

# ===== Chrome 설정 =====
CHROME_VERSION = 146  # Chrome 버전 (chrome://version 에서 확인)

# ═══════════════════════════════════════════════════════════
import time
import os
import sys
import glob
import pyperclip
import keyboard
import logging
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException,
)

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('naver_publish_v103.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


# ═══════════════════════════════════════════════════════════
# 경로 설정
# ═══════════════════════════════════════════════════════════

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(SCRIPT_DIR, "input")
SELECTORS_FILE = os.path.join(SCRIPT_DIR, "selectors.json")


def load_selectors():
    with open(SELECTORS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def find_design_file():
    """input/ 폴더에서 naver_*.json 찾기"""
    if not os.path.exists(INPUT_DIR):
        print(f"❌ input/ 폴더가 없습니다. 만들어주세요: {INPUT_DIR}")
        sys.exit(1)

    pattern = os.path.join(INPUT_DIR, "naver_*.json")
    files = glob.glob(pattern)

    if not files:
        print(f"❌ input/ 폴더에 naver_*.json 파일이 없습니다.")
        print(f"   폴더: {INPUT_DIR}")
        sys.exit(1)

    if len(files) == 1:
        return files[0]

    print("\n📋 설계도 파일이 여러 개 있습니다:")
    for i, f in enumerate(files):
        print(f"  [{i + 1}] {os.path.basename(f)}")
    choice = input("\n번호를 선택하세요: ").strip()
    try:
        return files[int(choice) - 1]
    except (ValueError, IndexError):
        print("❌ 잘못된 선택입니다.")
        sys.exit(1)


def load_design(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# ═══════════════════════════════════════════════════════════
# 드라이버 설정 + 로그인
# ═══════════════════════════════════════════════════════════


def find_patched_driver():
    """이미 패치된 chromedriver를 찾아서 반환 (속도 개선)"""
    cache_dir = os.path.join(os.environ.get("APPDATA", ""), "undetected_chromedriver")
    patched = os.path.join(cache_dir, "undetected_chromedriver.exe")
    if os.path.exists(patched):
        return patched
    return None


def setup_driver():
    """undetected_chromedriver 기반 크롬 드라이버 설정"""
    logging.info("🚀 크롬 드라이버 시작...")

    options = uc.ChromeOptions()

    # 봇 탐지 방지 옵션
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')

    # 비밀번호 저장 팝업 비활성화
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "safebrowsing.enabled": "false",
        "password_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)

    # ✅ 전용 프로필 (로그인 세션 유지)
    profile_path = os.path.join(SCRIPT_DIR, "NaverBlogProfile")

    # ✅ 패치된 드라이버 캐시 재사용 (50초 → 3초)
    patched = find_patched_driver()
    if patched:
        logging.info(f"⚡ 패치 캐시 발견 → 빠른 시작")
        driver = uc.Chrome(
            options=options,
            version_main=CHROME_VERSION,
            user_data_dir=profile_path,
            driver_executable_path=patched
        )
    else:
        logging.info("📥 첫 실행 — 드라이버 다운로드+패치 중 (1회만 느림)...")
        driver = uc.Chrome(
            options=options,
            version_main=CHROME_VERSION,
            user_data_dir=profile_path
        )

    driver.implicitly_wait(2)

    # 자동화 방지 우회
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    logging.info("✅ 크롬 드라이버 시작 성공!")
    return driver


def naver_login(driver, username, password):
    """네이버 로그인 - pyperclip 복사+붙여넣기 (v.211 검증 방식)"""
    try:
        driver.get("https://nid.naver.com/nidlogin.login")
        logging.info("로그인 페이지 접속")
        time.sleep(3)

        # 이미 로그인 상태면 스킵
        if "nid.naver.com/nidlogin" not in driver.current_url:
            logging.info("✅ 이미 로그인되어 있습니다 (프로필 세션 유지)")
            return True

        # ID 입력
        id_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id"))
        )
        id_input.clear()
        time.sleep(1)

        logging.info("아이디 입력 중...")
        pyperclip.copy(username)
        id_input.click()
        time.sleep(0.3)
        id_input.send_keys(Keys.CONTROL, 'v')
        time.sleep(0.5)

        # 비밀번호 입력
        pw_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pw"))
        )
        pw_input.clear()
        time.sleep(0.5)

        logging.info("비밀번호 입력 중...")
        pyperclip.copy(password)
        pw_input.click()
        time.sleep(0.5)
        pw_input.send_keys(Keys.CONTROL, 'v')
        time.sleep(0.5)

        # 로그인 버튼 클릭
        logging.info("로그인 버튼 클릭...")
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "log.login"))
        )
        login_button.click()
        time.sleep(5)

        # 로그인 성공 여부 확인
        if "nid.naver.com/nidlogin" in driver.current_url:
            logging.error("❌ 로그인 실패: 로그인 페이지에 머물러 있음")
            return False

        logging.info("✅ 로그인 성공!")
        return True

    except Exception as e:
        logging.error(f"❌ 로그인 실패: {e}")
        return False


# ═══════════════════════════════════════════════════════════
# 헬퍼 함수 (v.102 동일)
# ═══════════════════════════════════════════════════════════


def wait_and_find(driver, selector, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )


def wait_and_click(driver, selector, timeout=10):
    el = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    el.click()
    return el


def js_click(driver, element):
    """JavaScript로 강제 클릭 (겹침 문제 우회)"""
    driver.execute_script("arguments[0].click();", element)


def paste_text_to_element(driver, element, text):
    element.click()
    time.sleep(0.2)
    pyperclip.copy(text)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(
        Keys.CONTROL
    ).perform()


def press_enter(driver, count=1):
    for _ in range(count):
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(0.1)


def switch_to_main_frame(driver, sel):
    """구버전 에디터용 iframe 진입"""
    driver.switch_to.default_content()
    frame = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, sel["iframe"]))
    )
    driver.switch_to.frame(frame)


def clear_overlays(driver):
    """에디터 오버레이/팝업 제거"""
    try:
        driver.execute_script("""
            document.querySelectorAll(
                '.se-popup-dim, .se-popup-dim-transparent, [class*="popup-dim"], [class*="help"], [class*="tooltip"], [class*="dimmed"], [class*="guide"]'
            ).forEach(function(el) { el.remove(); });
        """)
    except Exception:
        pass


# ═══════════════════════════════════════════════════════════
# 메인 동작 함수 (v.102 기반 + 캡션 개선)
# ═══════════════════════════════════════════════════════════


def input_title(driver, sel, title):
    print(f"\n📝 제목 입력: {title[:40]}...")
    title_el = wait_and_click(driver, sel["title"])
    time.sleep(sel["timing"]["after_click"])
    paste_text_to_element(driver, title_el, title)
    time.sleep(sel["timing"]["after_paste"])


def input_text(driver, sel, content):
    pyperclip.copy(content)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(
        Keys.CONTROL
    ).perform()
    time.sleep(sel["timing"]["after_paste"])
    press_enter(driver)
    time.sleep(sel["timing"]["after_click"])


def upload_image(driver, sel, image_path, description=None):
    """이미지 업로드 + 캡션 입력 (개선)"""
    abs_path = os.path.abspath(image_path)

    if not os.path.exists(abs_path):
        print(f"  ⚠️ 이미지 파일 없음: {abs_path}")
        return False

    # 사진 버튼 클릭
    photo_btn = driver.find_element(By.CSS_SELECTOR, sel["photo_button"])
    photo_btn.click()
    time.sleep(sel["timing"]["after_photo_click"])

    # file input 찾기 (동적 생성)
    try:
        file_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, sel["file_input"]))
        )
        file_input.send_keys(abs_path)
    except TimeoutException:
        print("  ⚠️ file input을 찾을 수 없습니다.")
        return False

    # 이미지 업로드 대기
    time.sleep(sel["timing"]["after_image_upload"])

    # ⭐ 캡션(설명) 입력 — 개선: WebDriverWait + JS 클릭 폴백
    if description:
        caption_css = sel["image_caption"]
        caption_timeout = sel["timing"].get("caption_wait_max", 10)

        try:
            # 캡션 요소가 나타날 때까지 대기
            WebDriverWait(driver, caption_timeout).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, caption_css)) > 0
            )
            time.sleep(1)  # 추가 안정화 대기

            captions = driver.find_elements(By.CSS_SELECTOR, caption_css)
            if captions:
                latest_caption = captions[-1]

                # 클릭 시도: 일반 → JS 폴백
                try:
                    latest_caption.click()
                except (ElementNotInteractableException, Exception):
                    js_click(driver, latest_caption)
                time.sleep(sel["timing"]["after_click"])

                # 텍스트 입력
                pyperclip.copy(description)
                ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(
                    Keys.CONTROL
                ).perform()
                time.sleep(sel["timing"]["after_paste"])

        except TimeoutException:
            print(f"  ⚠️ 캡션 요소 대기 시간 초과 ({caption_timeout}초)")
        except Exception as e:
            print(f"  ⚠️ 캡션 입력 실패: {e}")

    # 캡션에서 빠져나오기
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(0.2)
    ActionChains(driver).send_keys(Keys.END).perform()
    time.sleep(0.2)
    press_enter(driver)
    time.sleep(sel["timing"]["after_click"])

    return True


def input_tags_in_body(driver, sel, tags):
    """본문 끝에 해시태그 텍스트로 입력"""
    print(f"\n🏷️ 해시태그 입력: {len(tags)}개")
    
    # 해시태그 문자열 생성
    hashtag_line = " ".join(f"#{tag.lstrip('#')}" for tag in tags)
    
    # 본문 끝에 줄바꿈 후 해시태그 붙여넣기
    press_enter(driver, 2)
    time.sleep(0.3)
    pyperclip.copy(hashtag_line)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(
        Keys.CONTROL
    ).perform()
    time.sleep(sel["timing"]["after_paste"])
    
    print(f"  ✅ 해시태그 {len(tags)}개 입력 완료")


# ═══════════════════════════════════════════════════════════
# 메인 실행
# ═══════════════════════════════════════════════════════════


def main():
    print("=" * 55)
    print("  🚀 네이버 블로그 자동발행 스크립트 v.103")
    print("     (자동 로그인 + 신/구 에디터 호환)")
    print("=" * 55)

    # 1. 설정 로드
    sel = load_selectors()
    print(f"\n✅ 셀렉터 로드 완료 (업데이트: {sel['_updated']})")

    # 2. 설계도 로드
    design_path = find_design_file()
    design = load_design(design_path)

    print(f"\n📋 설계도: {os.path.basename(design_path)}")
    print(f"   제목: {design['meta']['title']}")
    print(f"   카테고리: {design['meta'].get('category', '미지정')}")
    print(f"   태그: {len(design['meta'].get('tags', []))}개")
    print(f"   스텝: {len(design['steps'])}개")

    text_count = sum(1 for s in design["steps"] if s["action"] == "paste_text")
    image_count = sum(
        1 for s in design["steps"] if s["action"] == "upload_image"
    )
    print(f"   ├── 텍스트: {text_count}개")
    print(f"   └── 이미지: {image_count}개")

    # 이미지 파일 존재 확인 (input/ 폴더 기준)
    missing = []
    for step in design["steps"]:
        if step["action"] == "upload_image":
            img_path = os.path.join(INPUT_DIR, step["file"])
            if not os.path.exists(img_path):
                missing.append(step["file"])
    if missing:
        print(f"\n⚠️ 이미지 파일 {len(missing)}개 누락:")
        for m in missing:
            print(f"   ❌ {m}")
        proceed = input("\n계속 진행하시겠습니까? (y/n): ").strip().lower()
        if proceed != "y":
            sys.exit(0)
    else:
        print(f"\n✅ 이미지 파일 {image_count}개 확인 완료")

    # ═══════════════════════════════════════════════════════
    # 3. Chrome 열기 + 자동 로그인
    # ═══════════════════════════════════════════════════════
    print("\n🌐 Chrome 브라우저를 엽니다...")
    driver = setup_driver()
    driver.maximize_window()

    # 자동 로그인
    print("\n🔐 네이버 자동 로그인...")
    if not naver_login(driver, AUTO_LOGIN_ID, AUTO_LOGIN_PW):
        print("\n❌ 자동 로그인 실패!")
        print("   브라우저에서 수동으로 로그인한 후 F8을 누르세요.")
        keyboard.wait("f8")

    # 글쓰기 페이지로 이동
    print("\n📝 글쓰기 페이지로 이동...")
    driver.get(sel["write_url"])
    time.sleep(5)

    # F8 대기
    print("\n" + "=" * 55)
    print("  📝 글쓰기 화면이 열렸습니다.")
    print("  ⚠️  알림창이 있으면 수동으로 닫아주세요.")
    print("  ✅ 준비되면 F8을 누르세요.")
    print("=" * 55)

    keyboard.wait("f8")
    print("\n▶️ 자동 입력을 시작합니다!\n")

    # ═══════════════════════════════════════════════════════
    # 4. 자동글쓰기
    # ═══════════════════════════════════════════════════════
    try:
        # 에디터 진입 (신/구 버전 자동 감지)
        mainframe_exists = len(driver.find_elements(By.ID, "mainFrame")) > 0

        if mainframe_exists:
            print("📌 구버전 에디터 (iframe) → mainFrame 진입")
            switch_to_main_frame(driver, sel)
        else:
            print("📌 신버전 에디터 (SPA) → 직접 접근")

        # 제목 입력
        input_title(driver, sel, design["meta"]["title"])
        print("✅ 제목 입력 완료")

        # 본문 영역으로 이동 (오버레이 제거 후)
        clear_overlays(driver)
        time.sleep(0.5)

        body_el = wait_and_find(driver, sel["body"])
        try:
            body_el.click()
        except Exception:
            js_click(driver, body_el)
        time.sleep(sel["timing"]["after_click"])
        print("✅ 본문 영역 진입 완료")

        # 설계도 순서대로 실행
        print(f"\n📝 본문 입력 시작 ({len(design['steps'])}스텝)")
        print("-" * 40)

        for i, step in enumerate(design["steps"]):
            step_num = f"[{i + 1}/{len(design['steps'])}]"

            if step["action"] == "paste_text":
                preview = step["content"][:50].replace("\n", " ")
                print(f"  {step_num} 📝 텍스트: {preview}...")
                input_text(driver, sel, step["content"])
                print(f"         ✅ 완료")

            elif step["action"] == "upload_image":
                img_path = os.path.join(INPUT_DIR, step["file"])
                print(
                    f"  {step_num} 🖼️ 이미지: {step['file']}"
                )
                ok = upload_image(
                    driver, sel, img_path, step.get("description")
                )
                if ok:
                    desc_preview = step.get("description", "")[:40]
                    print(f"         ✅ 완료 (설명: {desc_preview}...)")
                else:
                    print(f"         ⚠️ 실패 — 수동 삽입 필요")

            if (i + 1) % 10 == 0:
                print(f"\n  💾 {i + 1}스텝 완료. 잠시 대기...")
                time.sleep(1)

        print("-" * 40)
        print("✅ 본문 입력 완료!")

        # 해시태그 (본문 끝에 텍스트로)
        tags = design["meta"].get("tags", [])
        if tags:
            input_tags_in_body(driver, sel, tags)

        # 완료
        print("\n" + "=" * 55)
        print("  🎉 자동 입력이 완료되었습니다!")
        print("=" * 55)
        print("\n  👉 미리보기로 내용을 확인해주세요.")
        print("  👉 카테고리를 선택한 후 [발행] 버튼을 눌러주세요.")
        if design["meta"].get("category"):
            print(f"     (권장 카테고리: {design['meta']['category']})")

    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        print("   브라우저는 열린 상태로 유지됩니다.")
        print("   수동으로 나머지 작업을 진행해주세요.")
        import traceback
        traceback.print_exc()

    print("\n" + "-" * 55)
    input("  [Enter]를 누르면 브라우저를 닫습니다...")
    driver.quit()
    print("\n👋 완료!")


if __name__ == "__main__":
    main()
