


import glob
from pathlib import Path
from DRAGON.utils import load_plugins
import logging
from DRAGON import DRAGON

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "DRAGON/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("تم تنصيب السورس بنجاح")
print("قناة السورس @Dragon_2022_D")
print("[للتنصيب ](https://t.me/DRACULA_2023/670)")
if __name__ == "__main__":
    DRAGON.run_until_disconnected()
