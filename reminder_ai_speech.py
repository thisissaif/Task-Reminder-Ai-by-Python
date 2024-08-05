import schedule
import time
import pyttsx3
from plyer import notification

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def send_notification(task):
    """Function to send a desktop notification and speak the task."""
    notification.notify(
        title='Reminder',
        message=task,
        app_name='Reminder AI',
        timeout=10
    )
    speak(task)

def schedule_task(task, hours, minutes):
    """Function to schedule a task."""
    schedule.every().day.at(f"{hours:02d}:{minutes:02d}").do(send_notification, task)

def start_scheduler():
    """Function to start the scheduler."""
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for one minute before checking the schedule again

def main():
    """Main function to add tasks."""
    print("Welcome to Reminder AI!")
    
    while True:
        task = input("Enter the task you want to be reminded of (or type 'exit' to quit): ")
        if task.lower() == 'exit':
            break
        
        hours = int(input("Enter the hour (24-hour format): "))
        minutes = int(input("Enter the minutes: "))

        # Schedule the task
        schedule_task(task, hours, minutes)
        print(f"Task '{task}' scheduled for {hours:02d}:{minutes:02d}.")

    print("Exiting Reminder AI.")

if __name__ == "__main__":
    main()
    start_scheduler()
