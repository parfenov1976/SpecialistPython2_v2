## ТЗ “I-Bank” Часть-2

Дополнение к документу “ТЗ I-Bank Часть-1”


### Доработки

1. Необходимо добавить возможность просмотра всей истории движения денежных средств на счету клиента(поступление, списание, переводы)

### Формат вывода истории:

**Пополнение** +600 руб. \
**Списание** -400 руб \
**Пополнение** +1000 руб. \
**Перевод** -750 руб. на счет клиента: Петр \
**Поступление** +300 руб. со счета клиента: Александр \
...

### Рекомендации по реализации

Информацию о каждой операции (пополнение, списание и т.д.) хранив в виде отдельного объекта \
Все операции храним в списке