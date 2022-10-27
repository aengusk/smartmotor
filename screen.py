# COM speed 115200
# with SCL in D1 and SDA in D2

from machine import Pin, I2C
from time import sleep
from random import getrandbits
import ssd1306

class Screen(x,y,width=w, height=h):
	def __init__(self,scale=8, points=[],point=[0,0]):
		self.i2c=I2C(sda=Pin(4),scl=Pin(5))
		self.display=ssd1306.SSD1306_I2C(128,64,self.i2c)

		self.scale = scale
		self.points = points
		self.point = point
		self._xDatum  = x // Datum x position in screen coordinates
		self._yDatum  = y // Datum y position in screen coordinates
		self._xWidth  = w // Viewport width
		self._yHeight = h // Viewport height
	


	def rectangle(self, x, y):
		for i in range(self.scale*x, self.scale*(x+1)):
			for j in range(self.scale*y, self.scale*(y+1)):
				self.display.pixel(i, j, 1)
		self.display.show()

	def update(self):
		self.display.fill(0)
		for i in self.points:
			self.rectangle(*i)
		self.rectangle(*self.point)
		self.display.show()

	def stamp(self):
		test = [i[0] for i in self.points]
		if(not self.point[0] in test):
			self.points.append(list(self.point))

	def changepointrandomly(self):
		if(getrandbits(1)):
			if(getrandbits(1) and self.point[0] < 128/self.scale - 1):
				self.point[0] += 1
			elif(point[0] > 0):
				self.point[0] -= 1
		else:
			if(getrandbits(1) and self.point[1] < 64/self.scale - 1):
				self.point[1] += 1
			elif(self.point[1] > 0):
				self.point[1] -= 1
			
	def circle(self,x,y,r):
		if(r<=0): 
			return
		else:
			inTransaction=True
			f=1-r
			ddF_y=-2*r
			ddF_x=1
			xs=-1
			xe=0
			len=0

			first=True
			while (xe < --r):
				while(f<0):
					xe+=1
					f+=(ddF_x+=2)
				f += (ddF_y += 2)
				if(xe-xs>1):
					if(first):


  if ( r <= 0 ) return;

  //begin_tft_write();          // Sprite class can use this function, avoiding begin_tft_write()
  inTransaction = true;

    int32_t f     = 1 - r;
    int32_t ddF_y = -2 * r;
    int32_t ddF_x = 1;
    int32_t xs    = -1;
    int32_t xe    = 0;
    int32_t len   = 0;

    bool first = true;
    do {
      while (f < 0) {
        ++xe;
        f += (ddF_x += 2);
      }
      f += (ddF_y += 2);

      if (xe-xs>1) {
        if (first) {
          len = 2*(xe - xs)-1;
          drawFastHLine(x0 - xe, y0 + r, len, color);
          drawFastHLine(x0 - xe, y0 - r, len, color);
          drawFastVLine(x0 + r, y0 - xe, len, color);
          drawFastVLine(x0 - r, y0 - xe, len, color);
          first = false;
        }
        else {
          len = xe - xs++;
          drawFastHLine(x0 - xe, y0 + r, len, color);
          drawFastHLine(x0 - xe, y0 - r, len, color);
          drawFastHLine(x0 + xs, y0 - r, len, color);
          drawFastHLine(x0 + xs, y0 + r, len, color);

          drawFastVLine(x0 + r, y0 + xs, len, color);
          drawFastVLine(x0 + r, y0 - xe, len, color);
          drawFastVLine(x0 - r, y0 - xe, len, color);
          drawFastVLine(x0 - r, y0 + xs, len, color);
        }
      }
      else {
        ++xs;
        drawPixel(x0 - xe, y0 + r, color);
        drawPixel(x0 - xe, y0 - r, color);
        drawPixel(x0 + xs, y0 - r, color);
        drawPixel(x0 + xs, y0 + r, color);

        drawPixel(x0 + r, y0 + xs, color);
        drawPixel(x0 + r, y0 - xe, color);
        drawPixel(x0 - r, y0 - xe, color);
        drawPixel(x0 - r, y0 + xs, color);
      }
      xs = xe;
    } while (xe < --r);

  inTransaction = lockTransaction;
  end_tft_write();              // Does nothing if Sprite class uses this function
}

while(True):
	changepointrandomly()
	update()
	if(getrandbits(3) == 0):
		stamp()
	sleep(getrandbits(2)/6)

def swap(a,b):
	temp=a
	a=b
	b=temp



def drawFastHLine( x,  y,  w, color):
  x+= _xDatum;
  y+= _yDatum;

  // Clipping
  if ((y < _vpY) || (x >= _vpW) || (y >= _vpH)) return;

  if (x < _vpX) { w += x - _vpX; x = _vpX; }

  if ((x + w) > _vpW) w = _vpW - x;

  if (w < 1) return;

  begin_tft_write();

  setWindow(x, y, x + w - 1, y);

  pushBlock(color, w);

  end_tft_write();
}


def drawLine(x0,y0,x1,y1):
	inTranslation=True
	steep=abs(y1-y0) > abs(x1-x0)
	return steep

	if steep:
		swap(x0,y0)
		swap(x1,y1)

	if(x0>x1):
		swap(x0,x1)
		swap(x1,y1)

	dx = x1 - x0
	dy = abs(y1 - y0)

	err = dx >> 1
	ystep = -1
	xs = x0
	dlen = 0;

	if (y0 < y1):
		ystep = 1

  if (_vpOoB) return;

  //begin_tft_write();       // Sprite class can use this function, avoiding begin_tft_write()
  inTransaction = true;

  //x+= _xDatum;             // Not added here, added by drawPixel & drawFastXLine
  //y+= _yDatum;

  bool steep = abs(y1 - y0) > abs(x1 - x0);
  if (steep) {
    swap_coord(x0, y0);
    swap_coord(x1, y1);
  }

  if (x0 > x1) {
    swap_coord(x0, x1);
    swap_coord(y0, y1);
  }

  int32_t dx = x1 - x0, dy = abs(y1 - y0);;

  int32_t err = dx >> 1, ystep = -1, xs = x0, dlen = 0;

  if (y0 < y1) ystep = 1;

  // Split into steep and not steep for FastH/V separation
  if (steep) {
    for (; x0 <= x1; x0++) {
      dlen++;
      err -= dy;
      if (err < 0) {
        if (dlen == 1) drawPixel(y0, xs, color);
        else drawFastVLine(y0, xs, dlen, color);
        dlen = 0;
        y0 += ystep; xs = x0 + 1;
        err += dx;
      }
    }
    if (dlen) drawFastVLine(y0, xs, dlen, color);
  }
  else
  {
    for (; x0 <= x1; x0++) {
      dlen++;
      err -= dy;
      if (err < 0) {
        if (dlen == 1) drawPixel(xs, y0, color);
        else drawFastHLine(xs, y0, dlen, color);
        dlen = 0;
        y0 += ystep; xs = x0 + 1;
        err += dx;
      }
    }
    if (dlen) drawFastHLine(xs, y0, dlen, color);
  }

  inTransaction = lockTransaction;
  end_tft_write();
}