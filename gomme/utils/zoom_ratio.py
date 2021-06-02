import win32api
import win32con
import win32gui
import win32print


# Ayant remarquer que cela ne fonctionner pas sur mon ordinateur portable je me suis demandé d' ou provenait le problème
# J' ai compris que c' était un problème avec le zoom par default de windows sur les ordinateurs portable

def recuperer_resolution_reelle():
    """Je crée un fonction qui ne prend rien en argument mais nous renvoie la resolution de notre écran (int,int) """
    hDC = win32gui.GetDC(0)

    res_hori = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    res_verti = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)

    return res_hori, res_verti


def recuperer_resolution_ecran():
    """Je crée une fonction qui ne prend rien en argument mais nous renvoie nous renvoie la resolution de notre écran
    (int,int) en tenant compte du zoom appliqué par windows """
    res_hori = win32api.GetSystemMetrics(0)
    res_verti = win32api.GetSystemMetrics(1)

    return res_hori, res_verti


def coef_zoom():
    """Je crée une fonction qui ne prend rien en argument mais nous renvoie le coefficient de zoom """
    resolution_reelle = recuperer_resolution_reelle()
    resolution_ecran = recuperer_resolution_ecran()

    return round(resolution_reelle[0] / resolution_ecran[0], 2)
