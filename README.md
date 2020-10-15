# 2D-Visual-Odometry



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/nadavleh/Chess_AI">
  </a>

  <h3 align="center">Fishyfish</h3>

  <p align="center">
    This is simple python chess program written with pygame for the GUI. The chess AI uses minimax with alpha-beta prunning
    <br />
    <a href="https://github.com/nadavleh/Chess_AI"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/nadavleh/Chess_AI">View Demo</a>
    ·
    <a href="https://github.com/nadavleh/Chess_AI/issues">Report Bug</a>
    ·
    <a href="https://github.com/nadavleh/Chess_AI/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/nadavleh/2D-Visual-Odometry-/blob/main/ORB%20Matching.png)

In this project we assume a robot equiped with a downward facing camera. Given two consecutive images of the floor, at time t and t+1 respectivly, we aim to estimate the robot's transformation. The transformation itself is comprised of a rotation matrix around the center of the robot (and subsequently the image) and a translation in te 2D floor plane.
This tranformation can be easily found using a known set of matching points between image t and image t+1. This is done by invoking the openCV method cv2.drawMatches() which solves the 8 degrees of freedom equations required to obtain the homography matrix. There are many obtainable transformations, more specificly there are exactly "n choose 8" such transformations, given n matches between image t and t+1. In order to determine the best among these transformations, the method cv2.drawMatches() preforms the RANSAC algorithm by which it determins the optimal transformation (the one with least outliers).

Once the transformation is found we can easily extract the angle and translation the robot have made between the two states (i.e. the images). Using 3D homography to estimate the special case 2D transformation is somewhat wastefull (because we solve a much more difficult problem albeit our assumptions that "the robot makes only a 2D affine transformation"), yet it provides us with a tool to esimate the hoomography estimatio's validity by checking the homograph matrix entries which correspond to 3D transformation and scaling, and verifying that they are indeed close to 0 and 1 respectivley. This fact is mentioned in the code, so if you didnt follow this cumbersome explenations, follow the ode for brevity.

So, the homography estimation is pretty easy given matches of points between the two images (thanks to the great openCV API), however how do we obtain these matches? The implementation of this is again, veyr easy thanks o the great API, however the theory behind obtaining these matches is not in the scope of this explenation (googling "ORB detection" will satisfy the curiouse mind). Essentially we invoke the "ORB detector" (very similar to SIFT but free!) to match points of interrest between the two images, where points of interrest are essentially "corners" (e.g. steep gradients between neighboring pixel values may imlpy such a corner).

### Built With

* [opnCV]
* [Python 3.7.1]
* [numpy]

## Usage
To run this program you need to put the floor image in the same directory as the .py file. At the start of execution, the program will kindly ask you by how much you want the robot to move (i.e. rotation angle and (x,y) translation), then it transforms the given image in such way as to mimic what the robot will see once it has moved b the specified transformation (bascaly we transform the image using a reverse 2D transformation of the one the user gave as an input). Next, the algorithm preforms the same procedure as described above where the given image is the one taken at time t, and the transformed image is the one at ime t+1.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/nadavleh/repo.svg?style=flat-square
[forks-shield]: https://img.shields.io/github/forks/nadavleh/repo.svg?style=flat-square
[forks-url]: https://github.com/nadavleh/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/nadavleh/repo.svg?style=flat-square
[stars-url]: https://github.com/nadavleh/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/nadavleh/repo.svg?style=flat-square
[issues-url]: https://github.com/nadavleh/repo/issues
[license-shield]: https://img.shields.io/github/license/nadavleh/repo.svg?style=flat-square
[product-screenshot]: https://github.com/nadavleh/2D-Visual-Odometry-/blob/main/ORB%20Matching.png

