import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
  def runTest(self):
    widget = Widget("The widget")
    assert widget.size() == (50, 50), 'incorrect default size'

if __name__ == "__main__":
  testCase = DefaultWidgetSizeTestCase()

