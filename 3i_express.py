import pygame as p
import time
from pygame import mixer

class ueh(p.sprite.Sprite):  # Định nghĩa một lớp mới có tên là ueh, là một lớp con của pygame.sprite.Sprite.

    def __init__(self):  # Đây là hàm khởi tạo cho lớp ueh.
        super().__init__()  # Gọi hàm khởi tạo của lớp cha Sprite.
        self.x = 50  # Tọa độ x của shipper.
        self.y = HEIGHT / 2  # Tọa độ y của shipper.
        self.vel = 6  # Vận tốc di chuyển của shipper.
        self.width = 100  # Chiều rộng của shipper.
        self.height = 50  # Chiều cao của shipper.

        # HÌNH ẢNH

        self.ueh1 = p.image.load('shipper 1.png')  # Tải hình ảnh 'shipper 1.png' và gán cho self.ueh1.
        self.ueh2 = p.image.load('shipper 2.png')  # Tải hình ảnh 'shipper 2.png' và gán cho self.ueh2.
        self.ueh1 = p.transform.scale(self.ueh1, (100,100))  # Thay đổi kích thước hình ảnh self.ueh1 thành 150x150.
        self.ueh2 = p.transform.scale(self.ueh2, (100,100))  # Thay đổi kích thước hình ảnh self.ueh2 thành 150x150.

        self.image = self.ueh1  # Gán hình ảnh hiện tại của shipper là self.ueh1.
        self.rect = self.image.get_rect()  # Lấy đối tượng Rect từ hình ảnh hiện tại của shipper.
        self.mask = p.mask.from_surface(self.image)  # Tạo một đối tượng Mask từ hình ảnh hiện tại của shipper.

    def update(self):  # Hàm cập nhật trạng thái của shipper.
        self.movement()  # Gọi hàm di chuyển.
        self.correction()  # Gọi hàm điều chỉnh.
        self.checkCollision()  # Gọi hàm kiểm tra va chạm.
        self.rect.center = (self.x, self.y)  # Cập nhật tọa độ trung tâm của đối tượng Rect.

    def movement(self):  # Hàm di chuyển shipper.
        keys = p.key.get_pressed()  # Lấy trạng thái của tất cả các phím.
        if keys[p.K_LEFT]:  # Nếu phím mũi tên trái được nhấn...
            self.x -= self.vel  # Di chuyển shipper sang trái.
            self.image = self.ueh2  # Thay đổi hình ảnh của shipper.

        elif keys[p.K_RIGHT]:  # Nếu phím mũi tên phải được nhấn...
            self.x += self.vel  # Di chuyển shipper sang phải.
            self.image = self.ueh1  # Thay đổi hình ảnh của shipper.

        if keys[p.K_UP]:  # Nếu phím mũi tên lên được nhấn...
            self.y -= self.vel  # Di chuyển shipper lên trên.

        elif keys[p.K_DOWN]:  # Nếu phím mũi tên xuống được nhấn...
            self.y += self.vel  # Di chuyển shipper xuống dưới.

    def correction(self):  # Hàm điều chỉnh vị trí của shipper.
        if self.x - self.width / 2 < 0:  # Nếu shipper đi quá biên trái...
            self.x = self.width / 2  # Đặt lại vị trí của shipper.

        elif self.x + self.width / 2 > WIDTH:  # Nếu shipper đi quá biên phải...
            self.x = WIDTH - self.width / 2  # Đặt lại vị trí của shipper.

        if self.y - self.height / 2 < 0:  # Nếu shipper đi quá biên trên...
            self.y = self.height / 2  # Đặt lại vị trí của shipper.

        elif self.y + self.height / 2 > HEIGHT:  # Nếu shipper đi quá biên dưới...
            self.y = HEIGHT - self.height / 2  # Đặt lại vị trí của shipper.

    def checkCollision(self):  # Hàm kiểm tra va chạm.
        horse_check = p.sprite.spritecollide(self, horse_group, False, p.sprite.collide_mask)  # Kiểm tra va chạm giữa shipper và nhóm ngựa.
        if horse_check:  # Nếu có va chạm...
            explosion.explode(self.x, self.y)  # Gọi hàm nổ.



class horse(p.sprite.Sprite):  # Dòng này định nghĩa một lớp mới có tên 'horse', là một lớp con của 'p.sprite.Sprite'.
    def __init__(self, number):  # Đây là phương thức khởi tạo cho lớp. Nó nhận 'self' và 'number' làm tham số.
        super().__init__()  # Dòng này gọi phương thức khởi tạo của lớp cha 'p.sprite.Sprite'.

        if number == 1:  # Nếu tham số 'number' bằng 1, khối mã sau sẽ được thực thi.
            self.x = 400  # Đặt thuộc tính 'x' của thể hiện 'horse' thành 190.
            self.image = p.image.load(
                'horse1.png')  # Tải tệp hình ảnh có tên 'Slow horse.png' và gán nó cho thuộc tính 'image'.
            self.vel = -4  # Đặt thuộc tính 'vel' (vận tốc) của thể hiện 'horse' thành -4.
        elif number == 2:
            self.x = 580  # Đặt thuộc tính 'x' của thể hiện 'horse' thành 460.
            self.image = p.image.load(
                'horse2.png')  # Tải tệp hình ảnh có tên 'Fast horse.png' và gán nó cho thuộc tính 'image'.
            self.vel = 5  # Đặt thuộc tính 'vel' (vận tốc) của thể hiện 'horse' thành 5.
        elif number == 3:  # Nếu tham số 'number' không phải là 1, khối mã sau sẽ được thực thi.
            self.x = 1050  # Đặt thuộc tính 'x' của thể hiện 'horse' thành 460.
            self.image = p.image.load(
                'horse2.png')  # Tải tệp hình ảnh có tên 'Fast horse.png' và gán nó cho thuộc tính 'image'.
            self.vel = 4  # Đặt thuộc tính 'vel' (vận tốc) của thể hiện 'horse' thành 5.
        else:
            self.x = 1250  # Đặt thuộc tính 'x' của thể hiện 'horse' thành 460.
            self.image = p.image.load(
                'horse1.png')  # Tải tệp hình ảnh có tên 'Fast horse.png' và gán nó cho thuộc tính 'image'.
            self.vel = -5  # Đặt thuộc tính 'vel' (vận tốc) của thể hiện 'horse' thành 5.

        self.y = HEIGHT / 2  # Đặt thuộc tính 'y' của thể hiện 'horse' thành một nửa giá trị của 'HEIGHT'.
        self.width = 100  # Đặt thuộc tính 'width' (chiều rộng) của thể hiện 'horse' thành 100.
        self.height = 150  # Đặt thuộc tính 'height' (chiều cao) của thể hiện 'horse' thành 150.
        self.image = p.transform.scale(self.image, (self.width,
                                                    self.height))  # Thay đổi kích thước thuộc tính 'image' để phù hợp với các thuộc tính 'width' và 'height'.
        self.rect = self.image.get_rect()  # Lấy khu vực hình chữ nhật của thuộc tính 'image' và gán nó cho thuộc tính 'rect'.
        self.mask = p.mask.from_surface(
            self.image)  # Tạo một mặt nạ cho thuộc tính 'image' và gán nó cho thuộc tính 'mask'.

    def update(self):  # Hàm cập nhật trạng thái của đối tượng.
        self.movement()  # Gọi hàm di chuyển.
        self.rect.center = (self.x, self.y)  # Cập nhật tọa độ trung tâm của đối tượng Rect.

    def movement(self):  # Hàm di chuyển đối tượng.
        self.y += self.vel  # Tăng tọa độ y của đối tượng theo vận tốc.

        if self.y - self.height < 200:  # Nếu đối tượng đi quá biên trên...
            self.y = self.height + 200    # Đặt lại vị trí của đối tượng.
            self.vel *= -1  # Đổi hướng di chuyển.
            self.image = p.image.load('horse2.png')

        elif self.y + self.height / 2 > HEIGHT - 250:  # Nếu đối tượng đi quá biên dưới...
            self.y =  750  # Đặt lại vị trí của đối tượng.
            self.vel *= -1  # Đổi hướng di chuyển.
            self.image = p.image.load('horse1.png')


class Screen(p.sprite.Sprite):  # Định nghĩa một lớp mới có tên là Screen, là một lớp con của pygame.sprite.Sprite.
    def __init__(self):  # Đây là hàm khởi tạo cho lớp Screen.
        super().__init__()  # Gọi hàm khởi tạo của lớp cha Sprite.
        self.img1 = p.image.load('3i express.png')  # Tải hình ảnh 'Scene.png' và gán cho self.img1.
        self.img2 = p.image.load('You Win.png')  # Tải hình ảnh 'You Win.png' và gán cho self.img2.
        self.img3 = p.image.load('You lose.png')  # Tải hình ảnh 'You lose.png' và gán cho self.img3.

        self.img1 = p.transform.scale(self.img1,
                                      (WIDTH, HEIGHT))  # Thay đổi kích thước hình ảnh self.img1 thành WIDTHxHEIGHT.
        self.img2 = p.transform.scale(self.img2,
                                      (WIDTH, HEIGHT))  # Thay đổi kích thước hình ảnh self.img2 thành WIDTHxHEIGHT.
        self.img3 = p.transform.scale(self.img3,
                                      (WIDTH, HEIGHT))  # Thay đổi kích thước hình ảnh self.img3 thành WIDTHxHEIGHT.

        self.image = self.img1  # Gán hình ảnh hiện tại của đối tượng là self.img1.
        self.x = 0  # Tọa độ x của đối tượng.
        self.y = 0  # Tọa độ y của đối tượng.

        self.rect = self.image.get_rect()  # Lấy đối tượng Rect từ hình ảnh hiện tại của đối tượng.

    def update(self):  # Hàm cập nhật trạng thái của đối tượng.
        self.rect.topleft = (self.x, self.y)  # Cập nhật tọa độ góc trên bên trái của đối tượng Rect.

class point(p.sprite.Sprite):  # Định nghĩa một lớp mới có tên là point, là một lớp con của pygame.sprite.Sprite.
    def __init__(self, number):  # Đây là hàm khởi tạo cho lớp point.
        super().__init__()  # Gọi hàm khởi tạo của lớp cha Sprite.
        self.number = number  # Số thứ tự của điểm.

        if self.number == 1:  # Nếu số thứ tự của điểm là 1...
            self.image = p.image.load('cash.png')  # Tải hình ảnh 'green point.png' và gán cho self.image.
            self.visible = False  # Đặt trạng thái hiển thị của điểm là False.
            self.x = 1580  # Tọa độ x của điểm.

        else:  # Nếu số thứ tự của điểm không phải là 1...
            self.image = p.image.load('point.png')  # Tải hình ảnh 'white point.png' và gán cho self.image.
            self.visible = True  # Đặt trạng thái hiển thị của điểm là True.
            self.x = 50  # Tọa độ x của điểm.

        self.y = HEIGHT / 2  # Tọa độ y của điểm.
        self.image = p.transform.scale(self.image,(150,150))  # Thay đổi kích thước hình ảnh của điểm thành gấp đôi.
        self.rect = self.image.get_rect()  # Lấy đối tượng Rect từ hình ảnh của điểm.
        self.mask = p.mask.from_surface(self.image)  # Tạo một đối tượng Mask từ hình ảnh của điểm.

    def update(self):  # Hàm cập nhật trạng thái của điểm.
        if self.visible:  # Nếu điểm đang hiển thị...
            self.collision()  # Gọi hàm kiểm tra va chạm.
            self.rect.center = (self.x, self.y)  # Cập nhật tọa độ trung tâm của đối tượng Rect.

    def collision(self):  # Hàm kiểm tra va chạm.
        global SCORE, ueh  # Sử dụng biến toàn cục SCORE và ueh.

        point_hit = p.sprite.spritecollide(self, ueh_group, False,
                                          p.sprite.collide_mask)  # Kiểm tra va chạm giữa đối tượng hiện tại và nhóm ueh_group.
        if point_hit:  # Nếu có va chạm...
            self.visible = False  # Đặt trạng thái hiển thị của đối tượng là False.

            if self.number == 1:  # Nếu số thứ tự của đối tượng là 1...
                white_point.visible = True  # Đặt trạng thái hiển thị của white_point là True.
                if SCORE < 4 :  # Nếu SCORE nhỏ hơn 5...
                    SwitchLevel()  # Gọi hàm SwitchLevel().

                else:  # Nếu SCORE không nhỏ hơn 5...
                    ueh_group.empty()  # Xóa tất cả các đối tượng trong nhóm ueh_group.
                    DeleteOtherItems()  # Gọi hàm DeleteOtherItems().

                    EndScreen(1)  # Gọi hàm EndScreen() với tham số là 1.

            else:  # Nếu số thứ tự của đối tượng không phải là 1...
                green_point.visible = True  # Đặt trạng thái hiển thị của green_point là True.

class Explosion(object):  # Định nghĩa một lớp mới có tên là Explosion.
    def __init__(self):  # Đây là hàm khởi tạo cho lớp Explosion.
        self.costume = 1  # Số thứ tự của hình ảnh hiện tại.
        self.width = 140  # Chiều rộng của hình ảnh.
        self.height = 140  # Chiều cao của hình ảnh.
        self.image = p.image.load(
            'explosion' + str(self.costume) + '.png')  # Tải hình ảnh 'explosion1.png' và gán cho self.image.
        self.image = p.transform.scale(self.image, (
        self.width, self.height))  # Thay đổi kích thước hình ảnh thành self.width x self.height.
        self.sound = p.mixer.Sound('e.mp3')  # Tải file âm thanh.
    def explode(self, x, y):  # Hàm tạo hiệu ứng nổ.
        global audio_playing
        x = x - self.width / 2  # Điều chỉnh tọa độ x.
        y = y - self.height / 2  # Điều chỉnh tọa độ y.
        Deleteueh()  # Gọi hàm Deleteueh().
        audio_playing = False
        self.sound.play()  # Phát âm thanh khi hiệu ứng nổ kích hoạt.

        while self.costume < 9:  # Trong khi số thứ tự của hình ảnh nhỏ hơn 9...
            self.image = p.image.load('explosion' + str(
                self.costume) + '.png')  # Tải hình ảnh 'explosion' kèm theo số thứ tự và gán cho self.image.
            self.image = p.transform.scale(self.image, (
            self.width, self.height))  # Thay đổi kích thước hình ảnh thành self.width x self.height.
            win.blit(self.image, (x, y))  # Vẽ hình ảnh lên cửa sổ tại vị trí (x, y).
            p.display.update()  # Cập nhật hiển thị.

            self.costume += 1  # Tăng số thứ tự của hình ảnh lên 1.
            time.sleep(0.1)  # Dừng chương trình trong 0.1 giây.

        DeleteOtherItems()  # Gọi hàm DeleteOtherItems().
        EndScreen(0)  # Gọi hàm EndScreen() với tham số là 0.

def ScoreDisplay():  # Hàm hiển thị điểm số.
    global gameOn  # Sử dụng biến toàn cục gameOn.

    if gameOn:  # Nếu game đang chạy...
        score_text = score_font.render('score ' + str(SCORE) + ' / 5', True,
                                       (0, 0, 0))  # Tạo đối tượng TextSurface từ chuỗi 'score' + SCORE + ' / 5'.
        win.blit(score_text, (70,800))  # Vẽ đối tượng TextSurface lên cửa sổ tại vị trí (50, 10).

def checkPoint():  # Hàm kiểm tra các điểm.
    for point in points:  # Duyệt qua từng điểm trong danh sách points.
        if not point.visible:  # Nếu điểm không hiển thị...
            point.kill()  # Gọi hàm kill() của điểm.

        else:  # Nếu điểm đang hiển thị...
            if not point.alive():  # Nếu điểm không còn tồn tại trong nhóm...
                point_group.add(point)  # Thêm điểm vào nhóm point_group.

def SwitchLevel():  # Hàm chuyển cấp độ.
    global SCORE  # Sử dụng biến toàn cục SCORE.

    if slow_horse1.vel < 0:  # Nếu vận tốc của slow_horse nhỏ hơn 0...
        slow_horse1.vel -= 1  # Giảm vận tốc của slow_horse đi 1.

    else:  # Nếu vận tốc của slow_horse không nhỏ hơn 0...
        slow_horse1.vel += 1  # Tăng vận tốc của slow_horse lên 1.

    if fast_horse1.vel < 0:  # Nếu vận tốc của fast_horse nhỏ hơn 0...
        fast_horse2.vel -= 1  # Giảm vận tốc của fast_horse đi 1.

    else:  # Nếu vận tốc của fast_horse không nhỏ hơn 0...
        fast_horse1.vel += 1  # Tăng vận tốc của fast_horse lên 1.

    SCORE += 1  # Tăng SCORE lên 1.

def Deleteueh():  # Hàm xóa shipper.
    global ueh  # Sử dụng biến toàn cục ueh.

    ueh.kill()  # Gọi hàm kill() của shipper.
    screen_group.draw(win)  # Vẽ nhóm screen_group lên cửa sổ.
    horse_group.draw(win)  # Vẽ nhóm horse_group lên cửa sổ.
    point_group.draw(win)  # Vẽ nhóm point_group lên cửa sổ.

    screen_group.update()  # Cập nhật trạng thái của nhóm screen_group.
    horse_group.update()  # Cập nhật trạng thái của nhóm horse_group.
    point_group.update()  # Cập nhật trạng thái của nhóm point_group.

    p.display.update()  # Cập nhật hiển thị.

def DeleteOtherItems():  # Hàm xóa các đối tượng khác.
    horse_group.empty()  # Xóa tất cả các đối tượng trong nhóm horse_group.
    point_group.empty()  # Xóa tất cả các đối tượng trong nhóm point_group.
    points.clear()  # Xóa tất cả các điểm trong danh sách points.


def EndScreen(n):  # Hàm kết thúc màn hình.
    global gameOn  # Sử dụng biến toàn cục gameOn.

    gameOn = False  # Đặt trạng thái chạy của game là False.
    handle_audio()

    if n == 0:  # Nếu tham số n là 0...
        bg.image = bg.img3  # Thay đổi hình ảnh của bg thành bg.img3.

    elif n == 1:  # Nếu tham số n là 1...
        bg.image = bg.img2  # Thay đổi hình ảnh của bg thành bg.img2.

WIDTH = 1640  # Chiều rộng của cửa sổ.
HEIGHT = 1080  # Chiều cao của cửa sổ.

p.init()  # Khởi tạo Pygame.
p.mixer.init()
mixer.music.load('v.mp3')
mixer.music.play(-1)
win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('3i express')
clock = p.time.Clock()
# Load the audio icons
audio_on = p.image.load('on.png')
audio_off = p.image.load('off.png')
audio_on = p.transform.scale(audio_on, (50, 50))
audio_off = p.transform.scale(audio_off, (50, 50))

# Variable to track audio state
audio_playing = True

# Function to handle audio
def handle_audio():  # Hàm xử lý âm thanh.
    global audio_playing  # Sử dụng biến toàn cục audio_playing.
    if audio_playing:  # Nếu âm thanh đang phát...
        mixer.music.pause()  # Tạm dừng âm thanh.
        audio_playing = False  # Đặt trạng thái phát âm thanh là False.

    else:  # Nếu âm thanh không phát...
        mixer.music.unpause()  # Tiếp tục phát âm thanh.
        audio_playing = True  # Đặt trạng thái phát âm thanh là True.

SCORE = 0  # Điểm số ban đầu.
score_font = p.font.SysFont('comicsans', 40, True)  # Font chữ và kích thước chữ cho điểm số.

bg = Screen()  # Tạo một đối tượng Screen.
screen_group = p.sprite.Group()  # Tạo một nhóm sprite.
screen_group.add(bg)  # Thêm đối tượng Screen vào nhóm.

ueh = ueh()  # Tạo một đối tượng ueh.
ueh_group = p.sprite.Group()  # Tạo một nhóm sprite.
ueh_group.add(ueh)  # Thêm đối tượng ueh vào nhóm.

slow_horse1 = horse(1)  # Tạo một đối tượng horse với số thứ tự là 1.
fast_horse1 = horse(2)
slow_horse2 = horse(3)
fast_horse2 = horse(4)

# Tạo một đối tượng horse với số thứ tự là 2.
horse_group = p.sprite.Group()  # Tạo một nhóm sprite.
horse_group.add(slow_horse1, fast_horse1, slow_horse2, fast_horse2)  # Thêm các đối tượng horse vào nhóm.

green_point = point(1)  # Tạo một đối tượng point với số thứ tự là 1.
white_point = point(2)  # Tạo một đối tượng point với số thứ tự là 2.
point_group = p.sprite.Group()  # Tạo một nhóm sprite.
point_group.add(green_point, white_point)  # Thêm các đối tượng point vào nhóm.
points = [green_point, white_point]  # Tạo một danh sách chứa các đối tượng point.

explosion = Explosion()  # Tạo một đối tượng Explosion.


def display_menu():  # Function to display the menu
    menu_image = p.image.load('3i express.png')  # Tải hình ảnh menu.
    menu_font = p.font.SysFont('comicsans', 60, True)
    title = menu_font.render('3i express', True, (255, 156, 17))
    instruction = menu_font.render('Press SPACE to start', True, (255, 156, 17))
    win.blit(menu_image, (0  , 0 )) # Vẽ hình ảnh menu lên cửa sổ game.
    win.blit(title, (- title.get_width() // 2 + 800, HEIGHT // 3))
    win.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, HEIGHT // 2))
gameOn = False  # Trạng thái chạy của game.
run = True  # Biến điều khiển vòng lặp chính của game.
def game_loop():
    global run, gameOn
    while run:  # Vòng lặp chính của game.
        clock.tick(60)  # Đặt tốc độ cập nhật của game là 60 FPS.
        for event in p.event.get():  # Duyệt qua tất cả các sự kiện.
            if event.type == p.QUIT:  # Nếu sự kiện thoát game...
                run = False  # Kết thúc vòng lặp chính.
            if event.type == p.MOUSEBUTTONDOWN:  # Nếu sự kiện nhấn chuột...
                x, y = p.mouse.get_pos()  # Lấy tọa độ của con trỏ chuột.
                # Kiểm tra xem biểu tượng âm thanh có được nhấn không.
                if 70 <= x <= 160 and 900 <= y <= 1200:
                    handle_audio()  # Gọi hàm xử lý âm thanh.





        screen_group.draw(win)  # Vẽ nhóm screen_group lên cửa sổ game.

        ScoreDisplay()  # Gọi hàm hiển thị điểm số.
        checkPoint()  # Gọi hàm kiểm tra các điểm.

        horse_group.draw(win)  # Vẽ nhóm horse_group lên cửa sổ game.
        ueh_group.draw(win)  # Vẽ nhóm ueh_group lên cửa sổ game.
        point_group.draw(win)  # Vẽ nhóm point_group lên cửa sổ game.
        # Vẽ biểu tượng âm thanh phù hợp.
        if audio_playing:  # Nếu âm thanh đang phát...
            win.blit(audio_on, (70,900))  # Vẽ biểu tượng âm thanh bật.

        else:  # Nếu âm thanh không phát...
            win.blit(audio_off, (70, 900))  # Vẽ biểu tượng âm thanh tắt.
        horse_group.update()  # Cập nhật trạng thái của nhóm horse_group.
        ueh_group.update()  # Cập nhật trạng thái của nhóm ueh_group.
        point_group.update()  # Cập nhật trạng thái của nhóm point_group.

        screen_group.update()  # Cập nhật trạng thái của nhóm screen_group.

        p.display.update()  # Cập nhật hiển thị.

while run:
    clock.tick(60)

    for event in p.event.get():

        if event.type == p.QUIT:
            p.quit()
            quit()
    keys = p.key.get_pressed()
    if keys[p.K_SPACE]:  # If space key is pressed, start the game
        gameOn = True


    if gameOn:
        game_loop()  # Start the game loop when gameOn is True
    else:
        display_menu()  # Display the menu when gameOn is False

    p.display.update()
