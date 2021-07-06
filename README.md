# Prudence
Prudence is an OSINT tool to look if an email or each emails from a list of has been registered on Instagram.
It is useful to check if an email or emails from a list are on Instagram.
I created it initially for me to look what email was registered on Instagram with a list of a lot the combinations of an email I found censored.

### Setup
```bash
git clone https://github.com/novitae/Prudence
cd instagram-activity/
pip install -r requirements.txt
```

### Usage
The usage is really simple :
```bash
python3 prudence.py
```
Then the program asks you directly what do you want to do.
Note that I only tested importing lists in .txt format,
so if it don't works with other formats, try to switch to .txt :)

### Module
The essential module to make this program run is holehe from Megadose.
If you ran requirement.txt, it should be installed, but if it's not,
you can download it by :

```bash
git clone https://github.com/megadose/holehe.git
cd holehe/
python3 setup.py install
```

Also check others https://github.com/megadose repositories, he's doing a really great work.
