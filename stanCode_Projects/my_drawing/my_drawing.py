"""
File: Karel
Name: David
----------------------
This program imitates the cover of the assignment 1 of stanCode SC001.
In addition, this program draws a Karel robot to show respect to Karel's author.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    This program imitates the cover of the assignment 1 of stanCode SC001
    and draws a Karel robot to show respect to Karel's author.
    """
    # Window
    window = GWindow(width=600, height=750, title="Karel")

    # Texts above Karel the robot.
    title = GLabel("stanCode")
    title.color = "darkred"
    title.font = "-80"
    window.add(title, x=(window.width-title.width)/2, y=110)
    sub_title = GLabel("標   準   程   式   教   育   機   構")
    sub_title.color = "darkred"
    sub_title.font = "-25"
    window.add(sub_title, x=(window.width-sub_title.width)/2, y=140)
    name = GLabel("Karel")
    name.color = "darkslategray"
    name.font = "-70"
    window.add(name, x=(window.width-name.width)/2, y=250)
    school = GLabel("Stanford University")
    school.color = "darkslategray"
    school.font = "-20"
    window.add(school, x=(window.width-school.width)/2, y=300)

    # Karel the robot
    # Karel's head
    head = GOval(width=school.width+30, height=(school.width+70)/2)
    head.filled = True
    head.fill_color = "lightgray"
    window.add(head, x=(window.width-head.width)/2, y=330)
    # Karel's left eye
    l_eye = GRect(head.width/5.5, head.width/5.5)
    l_eye.filled = True
    l_eye.fill_color = "blue"
    window.add(l_eye, head.x+head.width*0.23, head.y+head.height*0.4)
    # Karel's right eye
    r_eye = GRect(head.width / 5.5, head.width / 5.5)
    r_eye.filled = True
    r_eye.fill_color = "blue"
    window.add(r_eye, head.x+head.width*0.6, head.y+head.height*0.4)
    # Karel's body
    body = GRect(head.width, head.height*1.7)
    body.filled = True
    body.fill_color = "blue"
    window.add(body, head.x, head.y+head.height)
    # Karel's left shoulder
    l_shoulder = GRect(body.width/5, body.width/10)
    l_shoulder.color = "white"
    l_shoulder.filled = True
    l_shoulder.fill_color = "white"
    window.add(l_shoulder, body.x, body.y)
    # Karel's right shoulder
    r_shoulder = GRect(body.width/5, body.width/10)
    r_shoulder.color = "white"
    r_shoulder.filled = True
    r_shoulder.fill_color = "white"
    window.add(r_shoulder, body.x+body.width-r_shoulder.width, body.y)
    # Karel's left shoulder
    l_arm = GRect(l_shoulder.width, body.height*2/3)
    l_arm.filled = True
    l_arm.fill_color = "lime"
    window.add(l_arm, body.x-l_arm.width, body.y+l_shoulder.height*2)
    # Karel's right arm
    r_arm = GRect(l_shoulder.width, body.height * 2 / 3)
    r_arm.filled = True
    r_arm.fill_color = "lime"
    window.add(r_arm, body.x + body.width, body.y + l_shoulder.height * 2)
    # Karel's left feet
    l_feet = GOval(body.width/3, body.width/3.8)
    l_feet.filled = True
    l_feet.fill_color = "red"
    window.add(l_feet, body.x, body.y+body.height)
    # Karel's right feet
    r_feet = GOval(body.width / 3, body.width / 3.8)
    r_feet.filled = True
    r_feet.fill_color = "red"
    window.add(r_feet, body.x+body.width-r_feet.width, body.y + body.height)
    # The letter k on Karel's body
    k1 = GLine(body.x+body.width/3, body.y+l_shoulder.height*2, body.x+body.width/3, body.y+body.height*0.9)
    window.add(k1)
    k2 = GLine(body.x+body.width/3, body.y+body.height/2, body.x+body.width*2/3, body.y+l_shoulder.height*2)
    window.add(k2)
    k3 = GLine(body.x + body.width / 3, body.y + body.height / 2, body.x + body.width * 2 / 3, body.y+body.height*0.9)
    window.add(k3)


if __name__ == '__main__':
    main()
