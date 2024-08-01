class Print:
    def __init__(self, printData, blockPosition):
        """This block prints information in console."""
        self.printData = printData
        self.blockPosition = blockPosition
        self.blockData = f'print({printData})'
class Comment:
    def __init__(self, printData, blockPosition):
        """This block adds comment for your code."""
        self.printData = printData
        self.blockPosition = blockPosition
        self.blockData = f'-- {printData}'
class NewVariable:
    def __init__(self, printData, blockPosition):
      """This block creates new variable."""
      self.printData = printData
      self.blockPosition = blockPosition
      self.blockData = f'{printData[0]} = {printData[1]}'
class NewFunction:
    def __init__(self, printData, blockPosition):
        """This block creates new function."""
        self.printData = printData
        self.blockPosition = blockPosition
        self.blockData = f'function {printData[0]}{printData[1]}'
class SetWindowName:
    def __init__(self, printData, blockPosition):
       """This block sets name of game's window."""
       self.printData = printData
       self.blockPosition = blockPosition
       self.blockData = f'love.window.setTitle({printData})'
class Exit:
    def __init__(self, printData, blockPosition):
       """This block make game close."""
       self.printData = printData
       self.blockPosition = blockPosition
       self.blockData = f'love.event.quit({printData})'
class Fullscreen:
    def __init__(self, printData, blockPosition):
       """This block switches fullscreen mode."""
       self.printData = printData
       self.blockPosition = blockPosition
       self.blockData = f'love.window.setFullscreen({printData})'
class NewImage:
    def __init__(self, printData, blockPosition):
       """This block creates new image(sprite)."""
       self.printData = printData
       self.blockPosition = blockPosition
       self.blockData = f'{printData[0]} = love.graphics.newImage({printData[1]})'
class Draw:
    def __init__(self, printData, blockPosition):
       """This block draws image(sprite)"""
       self.printData = printData
       self.blockPosition = blockPosition
       self.blockData = f'love.graphics.draw({printData[0]}, {printData[1]}, {printData[2]})'
...