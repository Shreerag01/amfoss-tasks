import 'package:flame/components.dart';
import 'directions.dart';

class BunnyPlayer extends SpriteComponent with HasGameRef {
  BunnyPlayer() : super(size: Vector2.all(150.0));

  @override
  Future<void> onLoad() async {
    super.onLoad();
    sprite = await gameRef.loadSprite('bunny.png');
    position = gameRef.size;
  }

  Direction direction = Direction.none;

  @override
  void update(double dt) {
    super.update(dt);
    updatePosition(dt);
  }

  updatePosition(double dt) {
    switch (direction) {
      case Direction.up:
        position.y--;
        break;
      case Direction.down:
        position.y++;
        break;
      case Direction.left:
        position.x--;
        break;
      case Direction.right:
        position.x++;
        break;
      case Direction.none:
        break;
    }
  }
}

  /**updatePosition(double dt) {
    switch (direction) {
      case Direction.up:
        if (position.y < 10) {
          break;
        } else {
          position.y -= 2;
          break;
        }
      case Direction.down:
        if (position.y > 940) {
          break;
        } else {
          position.y += 2;
          break;
        }
      case Direction.left:
        if (position.x < 10) {
          break;
        } else {
          position.x -= 2;
          break;
        }
      case Direction.right:
        if (position.x > 1780) {
          break;
        } else {
          position.x += 2;
          break;
        }
      case Direction.none:
        break;
    }
  }
}**/