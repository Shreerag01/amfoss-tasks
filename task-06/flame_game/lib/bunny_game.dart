import 'dart:ui';

import 'package:flame/game.dart';
import 'directions.dart';
import 'bunny_player.dart';
import 'bunny_world.dart';

class BunnyGame extends FlameGame {
  BunnyPlayer _bunnyPlayer = BunnyPlayer();
  BunnyWorld _bunnyWorld = BunnyWorld();
  @override
  Future<void> onLoad() async {
    super.onLoad();
    await add(_bunnyWorld);
    await add(_bunnyPlayer);
    _bunnyPlayer.position = Vector2(940, 910);
    camera.followComponent(_bunnyPlayer,
        worldBounds:
            Rect.fromLTRB(0, 0, _bunnyWorld.size.x, _bunnyWorld.size.y));
  }

  onArrowKeyChanged(Direction direction) {
    _bunnyPlayer.direction = direction;
  }
}
