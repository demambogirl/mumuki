set_vacio
set()
  un_set
{1, 2, 3, 4}
  otro_set
{1, 2, 3}
  otro_set.issubset(un_set)
True
  un_set.issubset(otro_set)
False
  set_vacio.add("hola")
  set_vacio
{'hola'}
  un_set.remove(4)
  un_set
{1, 2, 3}
  un_set.clear()
  un_set
set()
  un_set.add(5)
  un_set.add(5)
  un_set
{5}