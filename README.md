# EnvChem Analyzer Pro — Android APK

## 3 Ways to Get the APK

---

## Method 1 — GitHub Actions (FREE, no setup, recommended)

1. Upload this folder to a GitHub repository
2. Go to **Actions** tab → **Build EnvChem APK** → **Run workflow**
3. Wait ~30 min → Download APK from **Artifacts**

That's it. GitHub's servers build it for you for free.

---

## Method 2 — Docker (local, one command)

**Requires:** Docker Desktop

**Linux/Mac:**
```bash
chmod +x scripts/build_apk.sh
./scripts/build_apk.sh
```

**Windows:**
```batch
scripts\build_apk.bat
```

First run: ~20–40 min (downloads Android SDK/NDK ~3 GB)
Subsequent runs: ~3–5 min (cached)

Output: `EnvChemPro.apk` in this folder

---

## Method 3 — Manual (Linux only)

```bash
# Install dependencies
sudo apt-get install -y python3-pip build-essential git \
  openjdk-17-jdk unzip autoconf libtool libffi-dev libssl-dev \
  libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

pip install buildozer cython

# Build
buildozer android debug

# APK is in: bin/envchem-3.0-arm64-v8a-debug.apk
```

---

## Install APK on Android

### Option A — Direct transfer
1. Copy `EnvChemPro.apk` to phone (USB / Google Drive / WhatsApp)
2. Open file manager on phone → tap the APK
3. Allow "Install unknown apps" when prompted
4. Tap Install

### Option B — ADB (developer)
```bash
adb install EnvChemPro.apk
```

---

## App Features (fully offline after install)

| Screen | Features |
|---|---|
| **Home** | Navigation hub with 6 modules |
| **AI Analysis** | Keyword-based risk assessment, contamination scoring 0–100 |
| **Geo Indices** | CF · Igeo · EF · PLI · mCd · RI with formulas & classifications |
| **Physicochemical** | WQI (Weighted Arithmetic) · WHO/EPA compliance · 20+ parameters |
| **Background Levels** | Reference values for 13 metals (3 geochemical standards) |
| **Formulas** | All indices, classification tables, Tᵣ values |
| **CSV Analysis** | Load CSV from device storage → statistics on-device |

## App Specs
- **Package:** org.envchem.envchem
- **Min Android:** 7.0 (API 24)
- **Target:** Android 13 (API 33)
- **Architectures:** arm64-v8a, armeabi-v7a
- **Offline:** 100% — no internet required for analysis
- **Size:** ~50–80 MB installed

## Project Structure
```
envchem_apk/
├── buildozer.spec           ← Android build config
├── app/
│   ├── main.py              ← Kivy app (all screens)
│   ├── envchem.kv           ← KV layout
│   └── src/
│       ├── __init__.py
│       └── analytics.py     ← Geo indices, WQI, WHO compliance
├── icons/
│   ├── icon.png             ← 192×192 app icon
│   └── icon_512.png         ← 512×512 store icon
├── scripts/
│   ├── build_apk.sh         ← Linux/Mac build script
│   └── build_apk.bat        ← Windows build script
└── .github/
    └── workflows/
        └── build.yml        ← GitHub Actions (free cloud build)
```

## Geochemical Formulas Implemented
```
CF   = Cm ÷ Cb                           Hakanson (1980)
Igeo = log₂(Cn ÷ 1.5 × Bn)             Müller (1969)
EF   = (Csample/Cref) ÷ (Cbg/Cref_bg)  Buat-Ménard (1979)
PLI  = (CF₁×CF₂×…×CFₙ)^(1/n)          Tomlinson (1980)
mCd  = Σ(CFᵢ) ÷ n                      Hakanson (1980)
Eᵣ   = Tᵣ × CF  ·  RI = Σ(Eᵣ)         Hakanson (1980)
WQI  = Σ(wᵢ×qᵢ) ÷ Σwᵢ                 Weighted Arithmetic
```
