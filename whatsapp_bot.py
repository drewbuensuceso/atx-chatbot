#ui automator test for whatsapp messaging
import uiautomator2 as u2
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
log = logging.getLogger('whatsapp.bot')

def send_message():
    #test connection to device
    device_id = '7b0c54dd'
    recipient = 'RECIPIENT'
    msg = 'MESSAGE'
    target_app = ('com.whatsapp')

    d = u2.connect('7b0c54dd')
    log.info(f'ATX is connected to Device: {device_id}')

    if(not d.info.get('screenOn')):
        log.info(d.info.get('screenOn'))
        d.unlock()
        log.info('screen unlocked')

    if d.app_wait(target_app): #checks if app is running and closes it to go back to default state
        d.app_stop(target_app)

    d.app_start(target_app) #opens whatsapp
    d.xpath('//*[@resource-id="com.whatsapp:id/fab"]').click() #new message button
    d.xpath('//*[@resource-id="com.whatsapp:id/menuitem_search"]').click() #search bar
    d.send_keys(recipient, clear=True)
    d.xpath('//*[@text="Miriam"]').click()
    d.send_keys(msg)
    log.info('sending message')
    d.xpath('//*[@resource-id="com.whatsapp:id/send_container"]').click()
    log.info('sent message sucessfully')
    d.app_stop('com.whatsapp')
    log.info('turning off screen')
    d.screen_off