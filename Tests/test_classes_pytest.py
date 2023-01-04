from Classes.classes import Robot, Direction, Point, Asteroid


def test_create_robot():
    r = Robot()
    assert (isinstance(r, Robot))


def test_turn():
    # Test "regular right turn
    r = Robot(bearing=Direction.north)
    # Test regular right turn
    r.turn('turn-right')
    b = r.bearing
    assert (r.bearing == Direction.east)

    # Test "extreme" right turn
    r = Robot(bearing=Direction.west)
    r.turn('turn-right')
    b = r.bearing
    assert (r.bearing == Direction.north)

    # Test "regular left turn
    r = Robot(bearing=Direction.east)
    r.turn('turn-left')
    b = r.bearing
    assert (r.bearing == Direction.north)

    # Test "extreme" left turn
    r = Robot(bearing=Direction.north)
    r.turn('turn-left')
    b = r.bearing
    assert (r.bearing == Direction.west)


def test_move():
    # Test "regular move north
    r = Robot(position=Point(), bearing=Direction.north)
    # Test regular right turn
    r.move()
    assert (r.position.y == 1)

    # Test "regular move east
    r = Robot(position=Point(), bearing=Direction.east)
    # Test regular right turn
    r.move()
    assert (r.position.x == 1)

    # Test "regular" move south
    r = Robot(position=Point(), bearing=Direction.south)
    r.move()
    assert (r.position.y == -1)

    # Test "regular" move west
    r = Robot(position=Point(), bearing=Direction.west)
    # Test regular right turn
    r.move()
    assert (r.position.x == -1)

    # Test boundaries
    a = Asteroid(Point(1,1))
    # Test north boundary
    r = Robot(position=Point(1,1), bearing=Direction.north,asteroid=a)
    r.move()
    assert (r.position.y == 1)

    # Test east boundary
    r = Robot(position=Point(1, 1), bearing=Direction.east, asteroid=a)
    r.move()
    assert (r.position.x == 1)

    # Test south boundary
    a = Asteroid(Point(0,0))
    r = Robot(position=Point(0, 0), bearing=Direction.south, asteroid=a)
    r.move()
    assert (r.position.y == 0)

    # Test west boundary
    a = Asteroid(Point(0, 0))
    r = Robot(position=Point(0, 0), bearing=Direction.west, asteroid=a)
    r.move()
    assert (r.position.x == 0)