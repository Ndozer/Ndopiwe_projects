import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 730
screen_height = 410
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ben 10')

current_fighter = 1
total_fighter = 3
action_cooldown = 0
action_wait_time = 90
game_over = 0

font = pygame.font.SysFont('Times New Roman', 26)
big_font = pygame.font.SysFont('Times New Roman', 48)
red = (255, 0, 0)
green = (0, 255, 0)

bg_img = pygame.image.load('benbg.png').convert_alpha()

def display_text(text, font, text_col, x, y):
    hp = font.render(text, True, text_col)
    screen.blit(hp, (x, y))

def display_omnitrix(x, y):
    img = pygame.image.load('omnitrix.png').convert_alpha()
    scaled_img = pygame.transform.scale(img, (int(img.get_width() * 0.4), int(img.get_height() * 0.4)))
    screen.blit(scaled_img, (x, y))
    return scaled_img.get_rect(topleft=(x, y))

def display_bg():
    screen.blit(bg_img, (0, 0))
    display_text(f'{player.name.capitalize()} HP: {player.hp}', font, red, 10, 10)
    omnitrix_rect = display_omnitrix(620, 310)
    for count, i in enumerate(villains):
        display_text(f'{i.name}: {i.hp}', font, red, 420 + (count * 150), 10)
    if target_villain and target_villain.alive:
        pygame.draw.polygon(screen, (255, 255, 0), [
            (target_villain.rect.centerx - 8, target_villain.rect.top - 15),
            (target_villain.rect.centerx + 8, target_villain.rect.top - 15),
            (target_villain.rect.centerx, target_villain.rect.top - 5)
        ])
    return omnitrix_rect

class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions, speed):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.speed = speed
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.attack_cooldown = 0
        self.attack_wait_time = 60
        self.transform_timer = 0
        self.action = 'idle'
        self.images = {}
        self.load_images()
        self.image = self.images[self.action]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def keep_on_screen(self, screen_width):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
    def load_images(self):
        action_files = {
            'idle': f'{self.name}_standing.png',
            'move': f'{self.name}_run.png',
            'attack': f'{self.name}_punch.png',
            'transform': f'{self.name}_hero_time.png',
            'alien': f'{self.name}_alien.png'
        }
        for action, file_path in action_files.items():
            try:
                img = pygame.image.load(file_path).convert_alpha()
            except (pygame.error, FileNotFoundError):
                try:
                    img = pygame.image.load(f'{self.name}_standing.png').convert_alpha()
                except (pygame.error, FileNotFoundError):
                    try:
                        img = pygame.image.load(f'{self.name}.png').convert_alpha()
                    except (pygame.error, FileNotFoundError):
                        img = pygame.Surface((50, 50))
                        img.fill((255, 0, 0))
            scaled_img = pygame.transform.scale(
                img, (int(img.get_width() * 0.4), int(img.get_height() * 0.4)))
            self.images[action] = scaled_img

    def update_action(self, new_action):
        if new_action in self.images and self.action != new_action:
            self.action = new_action
            center = self.rect.center
            self.image = self.images[self.action]
            self.rect = self.image.get_rect()
            self.rect.center = center

    def attack(self, target):
        ran = random.randint(-5, 5)
        damage = self.strength + ran
        target.hp -= damage
        if target.hp <= 0:
            target.hp = 0
            target.alive = False

    def update_ai(self, target, speed=2, attack_range=60):
        if not self.alive or not target.alive:
            return
        distance = target.rect.centerx - self.rect.centerx
        if abs(distance) <= attack_range:
            self.attack_cooldown += 1
            if self.attack_cooldown >= self.attack_wait_time:
                self.update_action('attack')
                self.attack(target)
                self.attack_cooldown = 0
            else:
                if self.attack_cooldown > 15:  
                    self.update_action('idle')
        else:
            self.attack_cooldown = 0
            self.update_action('move')
            if distance > 0:
                self.rect.x += speed
            elif distance < 0:
                self.rect.x -= speed

    def display_ben(self):
        screen.blit(self.image, self.rect)

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def display_health(self, hp):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 130, 18))
        pygame.draw.rect(screen, green, (self.x, self.y, 130 * ratio, 18))
class Button():
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
    def draw(self):
        pygame.draw.rect(screen, (50, 50, 50), self.rect, border_radius=8)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2, border_radius=8)
        text_s = font.render(self.text, True, (255, 255, 255))
        text_rect = text_s.get_rect(center=self.rect.center)
        screen.blit(text_s, text_rect)
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
def trigger_transform():
    global player, alien_index
    if player == ben:
        chosen_alien = aliens[alien_index]
        chosen_alien.rect.center = player.rect.center
        chosen_alien.hp = player.hp
        player = chosen_alien
        player.update_action('idle')
        alien_index = (alien_index + 1) % len(aliens)
    else:
        ben.rect.center = player.rect.center
        ben.hp = player.hp
        player = ben
        player.update_action('idle')
def reset_game():
    global player, target_villain, game_over

    ben.hp = ben.max_hp
    ben.alive = True
    ben.rect.center = (130, 260)
    
    for alien in aliens:
        alien.hp = alien.max_hp
        alien.alive = True
        alien.rect.center = (130, 260)
        
    player = ben
    player.update_action('idle')
    
    vilgax.hp = vilgax.max_hp
    vilgax.alive = True
    vilgax.rect.center = (420, 270)
    vilgax.update_action('idle')
    
    kevin.hp = kevin.max_hp
    kevin.alive = True
    kevin.rect.center = (620, 270)
    kevin.update_action('idle')
    
    target_villain = vilgax
    game_over = False
ben = Fighter(130, 260, 'ben', 100, 10, 3, speed=3)
vilgax = Fighter(420, 270, 'vilgax', 80, 6, 1, speed=3)
kevin = Fighter(620, 270, 'kevin', 80, 6, 1, speed=3)

humung = Fighter(130, 260, 'humung', 100, 25, 3, speed=2)
xlr = Fighter(130, 260, 'xlr8', 100, 10, 3, speed=8)
heatblast = Fighter(130, 260, 'heatblast', 100, 12, 3, speed=3)
cannonbolt = Fighter(130, 260, 'cannonbolt', 100, 17, 3, speed=5)

player = ben
alien_index = 0

villains = [vilgax, kevin]
aliens = [humung, xlr, heatblast, cannonbolt]
target_villain = vilgax

ben_health = HealthBar(10, 40, ben.hp, ben.max_hp)
vilgax_health = HealthBar(420, 40, vilgax.hp, vilgax.max_hp)
kevin_health = HealthBar(570, 40, kevin.hp, kevin.max_hp)

restart_button = Button(screen_width // 2 - 75, screen_height // 2 + 30, 150, 45, 'RESTART')
game_over = False
win = False

run = True
while run:
    clock.tick(fps)
    omnitrix_rect = display_bg()
    ben_health.display_health(player.hp)
    if vilgax.alive:
        vilgax_health.display_health(vilgax.hp)
    if kevin.alive:
        kevin_health.display_health(kevin.hp)

    if player.hp <= 0:
        player.alive = False
        game_over = True
        win = False
    elif not any(v.alive for v in villains):
        game_over = True
        win = True

    if not game_over:
        keys = pygame.key.get_pressed()
        moving = False
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.rect.x -= player.speed
            moving = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.rect.x += player.speed
            moving = True

        player.keep_on_screen(screen_width)

        if player.action not in ('attack', 'transform'):
            if moving:
                player.update_action('move')
            else:
                player.update_action('idle')

        for villain in villains:
            if villain.alive:
                villain.update_ai(player, speed=2, attack_range=60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            
            if game_over:
                if restart_button.is_clicked(mouse_pos):
                    reset_game()
            else:
                if omnitrix_rect and omnitrix_rect.collidepoint(mouse_pos):
                    trigger_transform()
                for villain in villains:
                    if villain.rect.collidepoint(mouse_pos) and villain.alive:
                        target_villain = villain

        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                player.update_action('attack')
                closest_villain = None
                min_dist = 100
                for villain in villains:
                    if villain.alive:
                        dist = abs(player.rect.centerx - villain.rect.centerx)
                        if dist < min_dist:
                            min_dist = dist
                            closest_villain = villain
                            target_villain = villain
                if closest_villain:
                    player.attack(closest_villain)

            if event.key == pygame.K_SPACE:
                trigger_transform()

        if not game_over and event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                player.update_action('idle')

    if player.alive:
        player.display_ben()
    for villain in villains:
        if villain.alive:
            villain.display_ben()

    if game_over:
        overlay = pygame.Surface((screen_width, screen_height))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        if win:
            display_text('VICTORY!', big_font, (0, 255, 0), screen_width // 2 - 110, screen_height // 2 - 60)
        else:
            display_text('GAME OVER', big_font, (255, 0, 0), screen_width // 2 - 140, screen_height // 2 - 60)            
        restart_button.draw()
    pygame.display.update()

pygame.quit()