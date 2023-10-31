from produtos import Chip, Notebook, Instrument, MarcaChip, MarcaNotebook, MarcaInstrument
from inventario import Inventario


chip_intel = Chip('Intel Z790', '12345', 12.0, 34, MarcaChip.INTEL)
notebook_macbok = Notebook('MacBook', '54321', 1200.0, 3, MarcaNotebook.MACBOOK)
instrument_guitar = Instrument('Guitarra', '67890', 500.0, 67, MarcaInstrument.GUITAR)
inv = Inventario()

inv.add_to_inventory(chip_intel)
inv.add_to_inventory(notebook_macbok)
inv.add_to_inventory(instrument_guitar)

inv.sell_product('12345', 36)
print("\n" + "=" * 80 + "\n")

inv.check_products_inventory()
print("\n" + "=" * 80 + "\n")

inv.add_product("12345", 10)
print("\n" + "=" * 80 + "\n")

inv.check_products_inventory()

print("\n" + "=" * 80 + "\n")
inv.sell_product('12345', 36)
print("\n" + "=" * 80 + "\n")

inv.check_products_inventory()
print("\n" + "=" * 80 + "\n")
