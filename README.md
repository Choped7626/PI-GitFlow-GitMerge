# Git, GitMerge & GitFlow

Ahora, debemos mergear esta rama `feat/A` sobre `develop`. Revisaremos que todo esté correcto. Por ejemplo, este mensaje ha de ser eliminado en el commit a develop, ya que carecería de sentido en esa rama. Además, yo eliminaría también la última línea, ya que estamos precisamente mergeando esta feat.

Lo siguiente a hacer, será mergear la rama `feat/B`.

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

Tras entender el código, tendríamos que ver que, tal como se puede esperar, debe dar 90

Ahora, mergeamos la rama `feat/A`.