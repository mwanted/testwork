# testwork

Пока сделано все, кроме общения с прометеусом. Учитывая, что весь этот helm я сегодня увидел первы раз в жизни.... В общем я прекрасно вижу пути для улучшения, оптимизации, повышения читаемости, но это все только если успею. 

Формально функционал реализован. :)

### Сборка контейнера

```
$cd build
$./build.sh
```

результат будет залит в репозиторий, для чего разумеется туда надо залогиниться. Но в целом этот шаг можно пропустить, т.к. образ там уже есть залитый мною. 

helm-chart настроен на репозиторий docker.io/remidor/private, который не смотря на название -- публичный.

### деплой:

```
helm install testwork ./chart 
```

или:

```
helm install testwork ./chart --set databackend=sqlite
```

с селектором ноды:

helm install testwork ./chart --set nodeSelector=<selector>
