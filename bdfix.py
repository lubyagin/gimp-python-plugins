#!/usr/bin/python
# -*- coding: utf-8 -*-
# см. также http://habrahabr.ru/post/135863/
# "Как написать дополнение для GIMP на языке Python"

# Импортируем необходимые модули
from gimpfu import *

## fix
def bdfix(image, drawable, w0, c0, w1, c1):
  # for Undo
  pdb.gimp_context_push()
  pdb.gimp_image_undo_group_start(image)
  # border-0
  pdb.gimp_image_resize(image, image.width + w0*2, image.height + w0*2, w0, w0)
  cz = pdb.gimp_context_get_background()
  pdb.gimp_context_set_background(c0)
  pdb.gimp_image_flatten(image)
  pdb.gimp_context_set_background(cz)
  # border-1
  pdb.gimp_image_resize(image, image.width + w1*2, image.height + w1*2, w1, w1)
  cz = pdb.gimp_context_get_background()
  pdb.gimp_context_set_background(c1)
  pdb.gimp_image_flatten(image)
  pdb.gimp_context_set_background(cz)
  # Refresh
  pdb.gimp_displays_flush()
  # Undo
  pdb.gimp_image_undo_group_end(image)
  pdb.gimp_context_pop()

# Регистрируем функцию в PDB
register(
  "python-fu-bdfix", # Имя регистрируемой функции
  "Добавление рамки к изображению", # Информация о дополнении
  "Помещает вокруг изображения рамку", # Короткое описание выполняемых скриптом действий
  "Александр Лубягин", # Информация об авторе
  "Александр Лубягин", # Информация о правах
  "15.01.2015", # Дата изготовления
  "Добавить рамку", # Название пункта меню, с помощью которого дополнение будет запускаться
  "*", # Типы изображений, с которыми работает дополнение
  [
  (PF_IMAGE, "image", "Исходное изображение", None), # Указатель на изображение
  (PF_DRAWABLE, "drawable", "Исходный слой", None), # Указатель на слой
  (PF_INT, "w0", "Ширина рамки, px", "9"), # Ширина рамки
  (PF_COLOR, "c0",  "Цвет рамки", (255,255,255)), # Цвет рамки
  (PF_INT, "w1", "Ширина рамки, px", "1"), # Ширина рамки
  (PF_COLOR, "c1",  "Цвет рамки", (0,0,0)) # Цвет рамки
  ],
  [], # Список переменных которые вернет дополнение
  bdfix, menu="<Image>/ТЕСТ/") # Имя исходной функции, и меню, в которое будет помещён пункт

# Запускаем скрипт
main()
