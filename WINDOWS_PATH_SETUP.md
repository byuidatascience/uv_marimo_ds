# Windows PATH Setup Guide

If you've installed UV but get a "command not found" error when trying to run `uv`, you need to add UV to your Windows PATH. This guide will walk you through the process.

## Quick Check

First, let's verify if UV is installed but just not in your PATH:

1. Open PowerShell
2. Run this command to check if UV is installed:
   ```powershell
   Test-Path "$env:USERPROFILE\.cargo\bin\uv.exe"
   ```
3. If this returns `True`, UV is installed and you just need to add it to your PATH

## Adding UV to PATH (Step-by-Step)

### Method 1: Using PowerShell (Recommended)

This is the quickest way to add UV to your PATH permanently:

1. **Open PowerShell as Administrator**
   - Press `Win + X`
   - Select "Windows PowerShell (Admin)" or "Terminal (Admin)"

2. **Run this command to add UV to your user PATH:**
   ```powershell
   $uvPath = "$env:USERPROFILE\.cargo\bin"
   [Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";$uvPath", "User")
   ```

3. **Close and reopen PowerShell** (or any terminal)

4. **Verify it works:**
   ```powershell
   uv --version
   ```

### Method 2: Using Windows Settings (GUI)

If you prefer using the graphical interface:

#### For Windows 11:

1. **Open System Settings**
   - Press `Win + I` to open Settings
   - Search for "environment variables" in the search box
   - Click "Edit environment variables for your account"

2. **Edit the PATH Variable**
   - In the "User variables" section, find and select `Path`
   - Click the "Edit..." button

3. **Add UV Directory**
   - Click "New"
   - Add this path: `%USERPROFILE%\.cargo\bin`
   - Click "OK" to close each window

4. **Verify the Change**
   - Close and reopen any PowerShell or Command Prompt windows
   - Run: `uv --version`

#### For Windows 10:

1. **Open System Properties**
   - Right-click on "This PC" or "My Computer"
   - Select "Properties"
   - Click "Advanced system settings" on the left
   - Click "Environment Variables..." button

2. **Edit the PATH Variable**
   - In the "User variables" section, find and select `Path`
   - Click "Edit..."

3. **Add UV Directory**
   - Click "New" (or "Add" on older versions)
   - Add this path: `%USERPROFILE%\.cargo\bin`
   - Click "OK" to close each window

4. **Verify the Change**
   - Close and reopen any PowerShell or Command Prompt windows
   - Run: `uv --version`

## Alternative UV Locations

UV might be installed in different locations depending on how it was installed. Check these locations:

1. **Default UV installation:**
   ```
   %USERPROFILE%\.cargo\bin\uv.exe
   ```
   (Usually: `C:\Users\YourUsername\.cargo\bin\uv.exe`)

2. **If installed via pip:**
   ```
   %APPDATA%\Python\Scripts\uv.exe
   ```

3. **If you can't find it, search for it:**
   ```powershell
   Get-ChildItem -Path $env:USERPROFILE -Filter "uv.exe" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
   ```

## Troubleshooting

### Issue: Changes don't take effect

**Solution:** You must close and reopen your terminal (PowerShell, Command Prompt, or Terminal) for PATH changes to take effect.

### Issue: UV still not found after adding to PATH

**Solution:** 
1. Verify the UV executable exists at the path you added:
   ```powershell
   Get-Item "$env:USERPROFILE\.cargo\bin\uv.exe"
   ```

2. Check your PATH includes the directory:
   ```powershell
   $env:Path -split ';' | Select-String -Pattern 'cargo'
   ```

3. Try restarting your computer if the above steps don't work

### Issue: Permission denied errors

**Solution:** 
1. Run PowerShell as Administrator
2. Or try using the GUI method which doesn't require admin rights

### Issue: Spaces in username or path

**Solution:** If your Windows username contains spaces, use quotes:
```powershell
$uvPath = "`"$env:USERPROFILE\.cargo\bin`""
```

## Testing Your Setup

Once UV is in your PATH, test that everything works:

```powershell
# Check UV version
uv --version

# Try installing a package in a test directory
mkdir $env:TEMP\uv-test
cd $env:TEMP\uv-test
uv init
uv add requests
uv run python -c "import requests; print(requests.__version__)"
```

If all these commands work, you're all set! 🎉

## Need More Help?

If you're still having issues:

1. Check the [UV documentation](https://docs.astral.sh/uv/)
2. Make sure you have administrator rights on your computer
3. Contact your instructor or IT support
4. Try uninstalling and reinstalling UV

## Quick Reference Card

| Task | Command |
|------|---------|
| Check if UV is installed | `Test-Path "$env:USERPROFILE\.cargo\bin\uv.exe"` |
| Find UV location | `Get-ChildItem -Path $env:USERPROFILE -Filter "uv.exe" -Recurse -ErrorAction SilentlyContinue` |
| Check UV version | `uv --version` |
| View current PATH | `$env:Path -split ';'` |
| Reload PATH in current session | `$env:Path = [System.Environment]::GetEnvironmentVariable("Path","User")` |

---

Return to the [main README](README.md) for usage instructions.
