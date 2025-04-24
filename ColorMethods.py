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
    l = [16767081,5287936,16767081,16767081,9090236,65535,255,13349725,13349725,5287936,5287936,16767081,9090236,9090236,16738047,65535,5479927,13524638,13524638,5479927,13349725,5287936,16738047,65535,65535,5287936,255,16767081,11711154,255,16767081,13349725,5479927,65535,16738047,16767081,5479927,5479927,13524638,5287936,13524638,65535,65535,16738047,16738047,255,5479927,16738047,5479927,13349725,16738047,11711154,9090236,11711154,11711154,9090236,255,255,13524638,13524638,5479927,5479927,65535,255,11711154,5287936,13349725,255,13349725,16738047,65535,255,11711154,65535,5287936,16738047,13349725,9090236,9090236,16738047,11711154,5287936,11711154,9090236,16738047,5287936,13349725,255]
    m = ["69D8FF","00B050","69D8FF","69D8FF","BCB48A","FFFF00","FF0000","5DB3CB","5DB3CB","00B050","00B050","69D8FF","BCB48A","BCB48A","FF66FF","FFFF00","F79D53","9E5ECE","9E5ECE","F79D53","5DB3CB","00B050","FF66FF","FFFF00","FFFF00","00B050","FF0000","69D8FF","B2B2B2","FF0000","69D8FF","5DB3CB","F79D53","FFFF00","FF66FF","69D8FF","F79D53","F79D53","9E5ECE","00B050","9E5ECE","FFFF00","FFFF00","FF66FF","FF66FF","FF0000","F79D53","FF66FF","F79D53","5DB3CB","FF66FF","B2B2B2","BCB48A","B2B2B2","B2B2B2","BCB48A","FF0000","FF0000","9E5ECE","9E5ECE","F79D53","F79D53","FFFF00","FF0000","B2B2B2","00B050","5DB3CB","FF0000","5DB3CB","FF66FF","FFFF00","FF0000","B2B2B2","FFFF00","00B050","FF66FF","5DB3CB","BCB48A","BCB48A","FF66FF","B2B2B2","00B050","B2B2B2","BCB48A","FF66FF","00B050","5DB3CB","FF0000"]


    # for color in l:
    #     print(ColorMethods.rgb_to_hex(color))
    for color in m:
        print(ColorMethods.hex_to_rgb(color))

