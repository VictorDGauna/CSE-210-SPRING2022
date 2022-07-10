from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script, _is_game_over):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score_one, score_two = cast.get_actors("scores")
        food = cast.get_first_actor("foods")
        snakes = cast.get_actors("snakes")
        snakes_one = snakes[0]
        snakes_two = snakes[1]
        if not _is_game_over:
            snakes_one.grow_trail(1)
            snakes_two.grow_trail(1)
        segments1 = snakes_one.get_segments()
        segments2= snakes_two.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments1)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score_one)
        self._video_service.draw_actor(score_two)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()