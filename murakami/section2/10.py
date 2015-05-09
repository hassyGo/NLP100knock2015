# -*- coding: utf-8 -*-

#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ．


if __name__ == "__main__":

    f = open('hightemp.txt')
    lines = f.readlines()
    f.close()
    print len(lines)
