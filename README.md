# Blender
1. Download repo
2. Run blending.py file 
3. You will see the results of alpha blending and blending with changing the position of two images.

Math behind alpha blending
C = d*A + (1-d)*B

Where C is a new image made of blending B image over A with transparency d

## Blending in Python
### Inicialization of images as RGBA array
Here we create an image of size 100 x 200. Furthermore, each pixel has RGBA values, thats why 3rd dimention is of size 4.
```python
image_1 = np.zeros([100, 200, 4], dtype=np.uint8)
```
### Colouring the image
By default, our image has all RGBA values equal to zero, so it is white and fully transparent. To change its colour we change the RGBA values.
```python
image_1[:, :100] = [255, 128, 0, 255] #Orange left side
image_1[:, 100:] = [0, 0, 255, 255]   #Blue right side
```
Here, the dransparency is equal to 255, so the image will be 100% nontransparent.

We created two images for further blending:

![first_image](https://user-images.githubusercontent.com/61863994/80916740-ea8e7880-8d5a-11ea-8182-e99d842e623d.png)

![second_image](https://user-images.githubusercontent.com/61863994/80916765-0eea5500-8d5b-11ea-9793-57fd854a4492.png)
### Alpha blending
For alpha blending, we need to have so called transparency (alpha) coeffitient d. This coeffitient determines the transparency of the images that we blend.
```python
d = 0.5
```
Next, we are using the formula:
C = d*A + (1-d)*B
to blend the two images (image_1 and image_2) together. image_3, a resulting image was initialized in the same way as image_1.
```python
for x in range(200):
    for y in range(100):
        image_3[y, x] = d * image_2[y, x] + (1 - d) * image_1[y, x]
```
We pixel by pixel using two for loops and give the image_3 pixel value of blended pixel from image_1 and image_2.

The result (image_3) of blending the created images:

![alpha_blending](https://user-images.githubusercontent.com/61863994/80916793-422ce400-8d5b-11ea-93d6-c6ce8d543732.png)

### Shifting and blending
For the purpose of shifting and blending we created a background - image_4 of size 300 x 300. It was initialized in the same way as all previous images and it is fully transparent.
Then, we define the coordinates x and y (the left up corner) of both images that we will blend, and their blend transparency.
```python
#first image coordinates
x1_coord = 10
y1_coord = 80
#transparency
d_1 = 0.9
```
After that, we perform the blending of image_4 (our background) with image_1, again using two for loops to go pixel by pixel. Notice that we start the iterations from the coordinates that we defined above, not from 0, so our image will be placed just where we want it to be. We assign the value of a pixel of image_1 to corresponding pixel of image_4. Since the background is white and fully transparent, we can ignore it in the blending equation. The if statement cuts out the excess of image_1, if it is placed too far away to fit within the background.
```python
for x in range(x1_coord,200+x1_coord):
    for y in range(y1_coord,100+y1_coord):
        if(x < 300 and y <300):
            image_4[y, x] = d_1*image_1[y - y1_coord, x - x1_coord]
```
So now, image_4 is image_1 blended with the background. We want now to blend in the second picture and we do it in exactly same way as before. Here, the image_4 is already after the first blending, so it's not an empty background, but image_1 is on it. That is why we have to have the second component in our blending equation.
```python
for x in range(x2_coord,200+x2_coord):
    for y in range(y2_coord,100+y2_coord):
        if(x < 300 and y <300):
            image_4[y, x] = d_2*image_2[y - y2_coord, x - x2_coord]+(1-d_2)*image_4[y, x]
```
The result of shifting and blending the two created pictures:

![shift_result](https://user-images.githubusercontent.com/61863994/80916840-8d46f700-8d5b-11ea-90fd-dfaae8bb469d.png)
### Saving the picture to a file
We used following code to convert the picture from array to png and save it.
```python
img = Image.fromarray(image_1)
img.save('first_image.png')
```
It uses function from PIL package.
### Importing images
To use existing image we have to convert it first to a RGBA table. We do it, using a function from the numpy package.
```python
image_5 = np.array(Image.open('flower.jpg'))
```
### Size of an imported image
Although the mechanism behind blending two imported images is the same, in the range function as argument we put a numpy fuction that gives tupple of array dimentions of our image.
```python
for x in range(np.shape(image_5)[1]):
    for y in range(np.shape(image_5)[0]):
        image_5[y, x] = d * image_5[y, x] + (1 - d) * image_6[y, x]
```
As an example we blended the following two pictures together:

![lena](https://user-images.githubusercontent.com/61863994/80916890-c1bab300-8d5b-11ea-86be-7bb1c222d0be.jpg)

![flower](https://user-images.githubusercontent.com/61863994/80916905-d5feb000-8d5b-11ea-89ee-6213fe353ea1.jpg)

The result is as follows:

![lena_with_flower](https://user-images.githubusercontent.com/61863994/80916912-e4e56280-8d5b-11ea-97e8-c66da0fafa7a.png)

Converting equation to integers 
```python
for x in range(200):
    for y in range(100):
        image_clone_1[y, x] = image_1[y, x]
        image_clone_2[y, x] = image_2[y, x]
        image_3[y,x] = (alpha * image_clone_2[y, x] + (256 - alpha) * image_clone_1[y, x]) >> 8
```
