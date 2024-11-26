# 貪吃蛇遊戲
這是嵌入式系統作業8

- 目前支援以下控制器
    - 鍵盤輸入(wasd, space)
    - MPU6050(陀螺儀控制前後左右, GPIO 17腳位按鈕)
    - 任何實作 IContoller 介面的控制器

- 目前支援以下顯示器
    - Terminel 輸出
    - sense_hat 輸出
    - 任何實作 IDisplay 介面的顯示器

## 如何運作
預設是使用鍵盤輸入與Terminel輸出

1. 安裝 pynput 鍵盤輸入偵測
    ```sh
    pip install pynput
    ```
2. 執行snake_game.py
    ```sh
    python ./snake_game.py
    ```
3. 如何離開程式:
    
    ctrl + c 強制關閉程式即可

