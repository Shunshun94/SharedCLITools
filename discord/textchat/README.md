# テキストチャットなんかするやつ

## post

### 使い方

post.bat でも post.sh でもおなじ。

```
post.bat DiscordのToken チャネルのID
```

### 使用例

```
post.bat MzAyNDU1MTg4MzQ4NzNzNzk0.WPPhWV.M4cqMTmBNIjJpg-7s1Gd9QtyRbQ 302452071993442307 post
```

## get

### 使い方

```
get.bat DiscordのToken チャネルのID 
```

### 使用例

```
get.bat MzAyNDU1MTg4MzQ4NzNzNzk0.WPPhWV.M4cqMTmBNIjJpg-7s1Gd9QtyRbQ 974996931216556069
```

### 注意点

bot の MESSAGE CONTENT INTENT を ON にしていないといくつかの情報を取得できません。
[Message Content Privileged Intent FAQ](https://support-dev.discord.com/hc/en-us/articles/4404772028055) も確認してください。

