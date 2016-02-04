ymaps.ready(init);
function init(){ 
    var myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 11,
        controls: ['smallMapDefaultSet'],
    }, 
        {
        searchControlProvider: 'yandex#search'
    }),
    menu = $('<ul class="my-menu"/>');
    for (var i = 0, l = groups.length; i < l; i++) {
        createMenuGroup(groups[i]);
    }
    function createMenuGroup (group) {
        // Пункт меню.
        var menuItem = $('<li><a class="group-name" href="#">' + group.name + '</a></li>'),
        // Коллекция для геообъектов группы.
            collection = new ymaps.GeoObjectCollection(null, { preset: group.style }),
        // Контейнер для подменю.
            submenu = $('<ul class="submenu"></ul>');
        // Добавляем коллекцию на карту.
        myMap.geoObjects.add(collection);
        // Добавляем подменю.
        menuItem
            .append(submenu)
            // Добавляем пункт в меню.
            .appendTo(menu)
            // По клику удаляем/добавляем коллекцию на карту и скрываем/отображаем подменю.
            .find('a')
            .click(function() {
                var thisList = $(this).parent().find(".submenu");
                thisList.slideToggle('fast', function() {
                    if(thisList.is(":visible")) {
                        myMap.geoObjects.add(collection);  
                    } else { 
                        myMap.geoObjects.remove(collection);
                    }
                });
            });
    for (var j = 0, m = group.items.length; j < m; j++) {
        createSubMenu(group.items[j], collection, submenu);
        }
        }
    function createSubMenu (item, collection, submenu) {
        // Пункт подменю.
        var submenuItem = $('<li><a href="#">' + item.name + '</a></li>'),
        // Создаем метку.
            placemark = new ymaps.Placemark(item.center, { balloonContentBody: (
                '<h5 class="balloon-h5"><a class="balloon-link" target="_blank" href="' + item.url + '">' + item.head + 
                '</a></h5><p class="balloon-p">' + item.body + '</p>'
                )
        });
        // Добавляем метку в коллекцию.
        collection.add(placemark);
        // Добавляем пункт в подменю.
        submenuItem
            .appendTo(submenu)
            // При клике по пункту подменю открываем/закрываем баллун у метки.
            .find('a')
            .click(function () {
                myMap.panTo(item.center, {
                    flying: 0,
                    duration: 500
                });
                if ( !placemark.balloon.isOpen() ) {
                    placemark.balloon.open();
                } else { 
                    placemark.balloon.close(); 
                    }
            });
        }
    // Добавляем меню в тэг BODY.
    menu.appendTo($('#map-menu'));
    // Выставляем масштаб карты чтобы были видны все группы.
    myMap.setBounds(myMap.geoObjects.getBounds());
}

// Вычисление высоты карты
$(window).resize(function () {
    var h = $(window).height(),
        offsetTop = 185; // Отступ
    $('#map').css('height', (h - offsetTop));
}).resize();
