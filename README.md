# Git, GitMerge & GitFlow

En este commit base únicamente se ha de preparar el venv con
```bash
python3 -m venv .venv
```

Cargar el venv
**Bash:**
```bash
source .venv/bin/activate
```

**PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

Y ejecutar
```bash
python3 ./order_system.py
```

Tras entender el código, tendríamos que ver que, tal como se puede esperar, debe dar 75

Ahora, mergeamos la rama `feat/A`.