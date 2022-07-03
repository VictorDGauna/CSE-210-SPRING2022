import random
from game.shared.point import Point
from game.shared.color import Color
from game.casting.gems import Gems
from game.casting.cast import Cast

MAX_GEM = 40
FONT_SIZE = 35

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        velocity = self._keyboard_service.get_direction()
        velocity._y = 0
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")
        gems = cast.get_actors("gems")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        cell_size = self._video_service.get_cell_size()
        
        if len(gems) < MAX_GEM:
            if random.randrange(0,20) == 3:
                new_gem = Gems()
                new_gem.set_font_size(FONT_SIZE)
                
                column = int(max_x / cell_size)
                location = Point(random.randrange(column)*cell_size,0)
                new_gem.set_position(location)
                cast.add_actor("gems",new_gem)   
        for gem in gems:

            #move the gem
            gem.move_next(max_x, max_y)
            y = gem.get_position().get_y()
            
            
            
            color = Color(100,180,255)
            gem.set_color(color)
            #Check for collision or reaching the bottom of the screen
            if player.get_position().closing(gem.get_position(), cell_size):
                self._add_score(gem.get_points())
                cast.remove_actor("gems",gem)
            #remove the rock when it reaches the bottom of the screen
            elif y > max_y - cell_size:
                cast.remove_actor("gems",gem)
            
        # Update banner with score
        banner.set_text(f"Score: {self._get_score()}")

            
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
    def _add_score(self, points):
        """
            Adds points to score
            Args: self - an instance of director,
                points to add
        """
        self._score += points
    def _get_score(self):
        """
          Returns current score
          Args: self - an instance of director
        """
        return self._score 