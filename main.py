import flet as ft
import random
import os 


img_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),"img"
)


def main(page: ft.Page):
    images = ft.Row(expand=1, wrap=False, scroll="always")
    def click(e):
        
        page.add(images)
        i=random.randint(1, 61)
        images.controls.append(
            ft.Image(
                #src=f"/Users/user/Dropbox/Code/python/Flet/work/static/img/A_{i}.png",
                src=f"/img/A_{i}.png",
                width=400,
                height=900,
                fit=ft.ImageFit.FILL,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(1),
            )
        )
        
        page.update()
        
    def clean(e):
        for img in images.controls:
            images.controls.remove(img)
        page.update()  

    page.window_left=20
    page.window_top=20
    page.window_height = 1050
    page.window_width =500
    page.title = "觀音靈籤"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    
    
    b = ft.ElevatedButton(text="卜卦", on_click=click)     #就是按下去執行後面的函數
    c = ft.ElevatedButton(text="收回", on_click=clean)     #就是按下去執行後面的函數
    #page.add(ft.Row([b,c])) #排在同一行
    page.add(b,c,images)
    
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir='assets')
