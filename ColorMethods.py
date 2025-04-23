from dataclasses import dataclass

@dataclass
class ColorMethods:
    @staticmethod
    def rgb_to_tuple(rgb: int):
        assert 0 <= rgb < 16777216
        r = rgb % 256
        g = (rgb // 256) % 256
        b = ((rgb // 256) // 256) % 256
        return (r, g, b)
    
    @staticmethod
    def hex_to_rgb(hex: str):
        assert len(hex) == 6
        HEX = "0123456789ABCDEF"
        rgb = 0
        for c in f"{hex[4:6]}{hex[2:4]}{hex[0:2]}":
            rgb *= 16
            rgb += HEX.find(c)
        return rgb
    
    @staticmethod
    def tuple_to_hex(r: int, g: int, b: int):
        assert 0 <= r < 256
        assert 0 <= g < 256
        assert 0 <= b < 256
        HEX = "0123456789ABCDEF"
        return HEX[r // 16] + HEX[r % 16] + HEX[g // 16] + HEX[g % 16] + HEX[b // 16] + HEX[b % 16]
    
    @staticmethod
    def tuple_to_rgb(r: int, g: int, b: int):
        assert 0 <= r < 256
        assert 0 <= g < 256
        assert 0 <= b < 256
        return r + g * 256 + b * 256 * 256
    
    @staticmethod
    def rgb_to_hex(rgb: int):
        assert 0 <= rgb < 16777216
        HEX = "0123456789ABCDEF"
        r = rgb % 256
        g = (rgb // 256) % 256
        b = ((rgb // 256) // 256) % 256
        return HEX[r // 16] + HEX[r % 16] + HEX[g // 16] + HEX[g % 16] + HEX[b // 16] + HEX[b % 16]
    
    @staticmethod
    def hex_to_tuple(hex: str):
        assert len(hex) == 6
        HEX = "0123456789ABCDEF"
        rgb = 0
        for c in f"{hex[4:6]}{hex[2:4]}{hex[0:2]}":
            rgb *= 16
            rgb += HEX.find(c)
        r = rgb % 256
        g = (rgb // 256) % 256
        b = ((rgb // 256) // 256) % 256
        return (r, g, b)

if __name__ == "__main__":
    var = "AACDEF"
    print(var)

    var = ColorMethods.hex_to_rgb(var)
    print(var)
    var = ColorMethods.rgb_to_tuple(var)
    print(var)
    var = ColorMethods.tuple_to_hex(var[0], var[1], var[2])
    print(var)

    var = ColorMethods.hex_to_tuple(var)
    print(var)
    var = ColorMethods.tuple_to_rgb(var[0], var[1], var[2])
    print(var)
    var = ColorMethods.rgb_to_hex(var)
    print(var)
