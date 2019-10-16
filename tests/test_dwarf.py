from pyobjfile.mach_o import Mach


def setup_macho_dwarf():
    macho_path = "tests/data/hello.dSYM/Contents/Resources/DWARF/hello"
    macho = Mach(path=macho_path)
    slice1 = macho.get_architecture_slice_at_index(0)
    dw = slice1.get_dwarf()
    return dw


def setup_macho_dwarf_di():
    dwf = setup_macho_dwarf()
    di = dwf.get_debug_info()
    return di


def setup_macho_dwarf_get_dies():
    di = setup_macho_dwarf_di()
    units = di.get_compile_units()
    dies = []
    for cu in units:
        dies.extend(cu.get_dies())
    return dies


def test_get_dwarf():
    dwf = setup_macho_dwarf()
    assert dwf is not None


def test_get_debug_info():
    dwf = setup_macho_dwarf()
    di = dwf.get_debug_info()
    assert di is not None


def test_get_compile_units_01():
    di = setup_macho_dwarf_di()
    assert di is not None
    units = di.get_compile_units()
    assert 1 == len(units)


def test_get_compile_units_02():
    di = setup_macho_dwarf_di()
    assert di is not None
    units = di.get_compile_units()
    for unit in units:
        assert unit is not None


def test_get_dies():
    offsets = [11, 42, 67, 81, 95, 109, 110, 117, 122, 127, 134]
    dies = setup_macho_dwarf_get_dies()
    for idx, die in enumerate(dies):
        offset = offsets[idx]
        assert offset == die.offset


def test_get_base_type_char_01():
    char_die_offset = 127
    char_type_name = 'char'
    di = setup_macho_dwarf_di()
    cu = di.get_compile_units()[0]
    die = cu.get_die_with_offset(char_die_offset)
    assert char_type_name == die.get_name()


def test_get_base_type_char_02():
    char_die_offset = 127
    char_type_size = 1
    di = setup_macho_dwarf_di()
    cu = di.get_compile_units()[0]
    die = cu.get_die_with_offset(char_die_offset)
    assert char_type_size == die.get_byte_size()
