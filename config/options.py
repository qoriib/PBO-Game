class GameOption:
    CELL_SIZE = 50
    GRID_SIZE = 9
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 850
    BOARD_OFFSET_Y = 100
    BOARD_OFFSET_X = (SCREEN_WIDTH - GRID_SIZE * CELL_SIZE) // 2

    BACKGROUND_COLOR = (89, 134, 248)
    EMPTY_COLOR      = (248, 175, 221)
    GRID_LINE_COLOR  = (186, 148, 194)
    BIG_GRID_COLOR   = (205, 147, 183)
    TEXT_COLOR       = (50, 48, 48)
    
    BLOCK_IMAGE_PATH = "assets/blocks/"
    FONT_PATH = "assets/fonts/"
    MUSIC_PATH = "assets/musics/"