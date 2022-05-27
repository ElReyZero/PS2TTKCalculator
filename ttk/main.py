from ttk import getTTK
from modules import config as cfg

def main():
    print(getTTK('Betelgeuse 54-A', 1, 100))

if __name__ == '__main__':
    cfg.get_config()
    main()