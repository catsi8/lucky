import flet as ft
import random


def main(page: ft.Page):
    img = ft.Image(
        src=f"/code1.jpg",
        
    )
    images=ft.Image(src=f"./code1.jpg")
    page.add(img)
    def click(e):
        t.value = f"資料分別是: '{tb2.value}', '{tb3.value}', '{tb4.value}'"
        
        page.update()
        
    def show(e):
        t.value =random.randint(1, 10)
        
        page.update()    
    #ft.TextField表示有一個輸入框，ft.Text表示直接印在螢幕上,ft.ElevatedButton表示有一個按鈕
    t = ft.Text()
    #tb1 = ft.TextField(label="Standard")
    tb2 = ft.TextField(label="姓", hint_text="請輸入姓，例如：高",width=100)
    tb3 = ft.TextField(label="名", hint_text="請輸入名字，例如：大俠",width=200)
    tb4 = ft.TextField(label="手機", hint_text="請輸入手機號碼，例如；0980371712",width=300)
    b = ft.ElevatedButton(text="送出", on_click=click)     #就是按下去執行後面的函數
    page.add(ft.Row([tb2, tb3, tb4])) #排在同一行
    page.add(b, t)
    page.add()
    #d=ft.Text("你是好人")
    t2 = ft.ElevatedButton(text="按下去抽獎", on_click=show)     #就是按下去執行後面的函數
    page.add(t2)
    page.add(images)
    
    
ft.app(target=main)
