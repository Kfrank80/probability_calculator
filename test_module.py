from prob_calculator import Hat


class TestHat:

    def test_1(self):
        assert 1 == 1
        pass

    def test_init(self):
        hat1 = Hat(red=3, green=2)
        assert hat1.contents == ["red", "red", "red", "green", "green"]
        pass

    def test_draw(self):
        hat1 = Hat(red=3, green=2)
        assert len(hat1.draw(3)) == 3 and len(hat1.contents) == 2
        assert len(hat1.draw(3)) == 2
        pass
    pass
