import Widget
import unittest

class SimpleWidgetTestCase(unittest.TestCase):
  def setUp(self):
    self.widget = Widget.Widget()

class DefaultWidgetSizeTestCase(SimpleWidgetTestCase):
  def runTest(self):
    assert self.widget.getSize() == (40, 40), 'incorrect default size'

class WidgetResizeTestCase(SimpleWidgetTestCase):
  def runTest(self):
    self.widget.resize(100, 150)
    assert self.widget.getSize() == (100, 150), 'wrong size after resize'

if __name__ == "__main__":
  unittest.main()
