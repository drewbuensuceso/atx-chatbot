#ui automator test for whatsapp messaging
import uiautomator2 as u2
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
log = logging.getLogger('facebook.bot')

def send_message():
    #test connection to device
    device_id = '7b0c54dd'
    recipient = 'RECIPIENT NAME'
    msg = 'MESSAGE'
    target_app_url = ('facebook://fb.com')

    d = u2.connect('7b0c54dd')
    log.info(f'ATX is connected to Device: {device_id}')

    if(not d.info.get('screenOn')):
        log.info(d.info.get('screenOn'))
        d.unlock()
        log.info('screen unlocked')

    if(d.app_wait("com.facebook.katana")): #check if app is running:
        d.app_stop('com.facebook.orca')
        d.app_stop('com.facebook.katana')
        log.info('closing fb apps')

    d.open_url(target_app_url)
    d(resourceId="com.facebook.katana:id/(name removed)", description="Messaging").click() #opens messenger from facebook

    #inside messenger
    d(description="New Message").click() #create a message
    d.send_keys(recipient, clear=True) #type name of recipient
    d.implicitly_wait(5)
    first_result = d(index=3, className='android.view.ViewGroup')

    first_result.click()
    d(className='android.widget.EditText').click()
    d.send_keys(msg, clear=True)

    send_button = d(className="android.widget.FrameLayout", index=1, instance=2)
    #log.info(send_button.info)
    send_button.click()
    log.info("Message was sent successfully")
    #d.implicitly_wait(20)
    d.app_stop('com.facebook.orca')
    d.screen_off()