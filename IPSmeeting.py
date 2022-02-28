import sys
import time


class IPSMeeting:
    n = int(input('enter number of attendees: '))
    names = []
    states = []
    cities = []
    ids = []
    pins = []
    purpose = []


class getDetails(IPSMeeting):
    n = IPSMeeting.n
    names = IPSMeeting.names
    states = IPSMeeting.states
    cities = IPSMeeting.cities
    ids = IPSMeeting.ids
    pins = IPSMeeting.pins
    purpose = IPSMeeting.purpose
    for i in range(n):
        name = input("enter name of attendee number {}: ".format(i))
        names.append(name)
    for i in range(n):
        state = input("enter state of {}: ".format(names[i]))
        states.append(state)
    for i in range(n):
        city = input("enter city of {}: ".format(names[i]))
        cities.append(city)
    for i in range(n):
        id = int(input('enter ID of {}: '.format(names[i])))
        ids.append(id)
    for i in range(n):
        pin = int(input('enter pin code for address of {}: '.format(names[i])))
        pins.append(pin)
    for i in range(n):
        purp = input('enter purpose of meeting for {}: '.format(names[i]))
        purpose.append(purp)


obj = IPSMeeting()
obj1 = getDetails()


class Display(IPSMeeting):
    def showAll(self):
        print('----Meeting Attendees details----')

        for i in range(obj.n):
            print('Name: {}, State: {}, City: {}, Pin Code: {}, ID: {}'.format(obj1.names[i], obj1.states[i],
                                                                               obj1.cities[i], obj1.pins[i],
                                                                               obj1.ids[i]))
            print('Purpose of meeting for {} : {}'.format(obj1.names[i], obj1.purpose[i]))
            print('*' * 50)


obj2 = Display()
obj2.showAll()


class Select(IPSMeeting):
    metWith = []
    meetDuration = []
    meetIDs = []
    meetCount = 0
    m = sys.maxsize
    concl = []
    total = obj.n

    def selectPerson(self):
        for i in range(self.m):
            meetPerson = int(input("enter ID of peroson you want to meet: "))
            meetDur = int(input("enter the meeting duration for meeting with person {}".format(meetPerson)))
            meetID = 'mID-' + str(i)

            self.metWith.append(meetPerson)
            self.meetDuration.append(meetDur)
            self.meetIDs.append(meetID)

            time.sleep(meetDur)
            meetPurpose = input("what conclusion/purpose you achieved by meeting with {}: ".format(meetPerson))
            self.concl.append(meetPurpose)
            self.meetCount = self.meetCount + 1
            self.total = self.total-1
            if self.total == 0:
                print('No attendees left')
                break
            else:
                print('remaining = {}'.format(self.total))
                consent = input("Do you still want to meet another person: YES or NO:  ")
                if consent == 'YES':
                    continue
                elif consent == 'NO':
                    break


obj3 = Select()
obj3.selectPerson()


class FinalDisplay(Select):
    def __init__(self):
        print('\n')
        print('------  MEETING INFORMATION  ------')
        print('\n')
        print("Number of persons met = {}".format(obj3.meetCount))
        print('*' * 50)
        for i in range(obj3.meetCount):
            print('met with person no.: {}  ID : {}'.format(i, obj3.meetIDs[i]))

            print("meeting duration {} ".format(obj3.meetDuration[i]))
            ind = obj1.ids.index(obj3.metWith[i])
            print("NAME: {} ".format(obj1.names[ind]))
            print("STATE: {} ".format(obj1.states[ind]))
            print("CITY: {} ".format(obj1.cities[ind]))
            print("PINCODE: {} ".format(obj1.pins[ind]))
            print("PURPOSE: {} ".format(obj1.purpose[ind]))
            print("CONCLUSION : {} ".format(obj3.concl[i]))
            print('~~~~~~~~')


obj4 = FinalDisplay()

