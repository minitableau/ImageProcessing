import win32api
import win32con
import win32gui
import win32print


def recuperer_resolution_reelle():
    hDC = win32gui.GetDC(0)

    res_hori = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    res_verti = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)

    return res_hori, res_verti


def recuperer_resolution_ecran():

    res_hori = win32api.GetSystemMetrics(0)
    res_verti = win32api.GetSystemMetrics(1)

    return res_hori, res_verti


def get_screen_scale_rate():

    resolution_reelle = recuperer_resolution_reelle()
    resolution_ecran = recuperer_resolution_ecran()

    return round(resolution_reelle[0] / resolution_ecran[0], 2)
