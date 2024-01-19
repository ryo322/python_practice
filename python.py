def divide(a, b):
    try:
        print(f'計算結果： {a/b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        pass
    finally:
        print('すべての処理が正常に終了しました。')

print(divide(10, '5'))