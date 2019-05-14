    myrobot = legoev3('usb'); %Opens a new connection to a EV3
                                %robot on a USB port 
                                
    beep(myrobot); % Generate a beep 
    `
    mA = motor(myrobot, 'A'); %create an object for the motor A
    mA.Speed = -10; % we start with half the maximum power 
    mA.Speed = 0;
    start(mA); % this is actually the moment we start the motor
    stop(mA);
    stop(mA, 1);

mA = motor(myrobot, 'A');
mB = motor(myrobot, 'B');

mA.Speed = 50;
mB.Speed = 50;
start(mA);
start(mB);

mA.Speed = 0;
mB.Speed = 0;

myUltrasonicSensor = sonicSensor(myrobot);
val = readDistance(myUltrasonicSensor);
display (val); 

myColourSensor = colorSensor(myrobot,1); 
ambient=readLightIntensity(myColourSensor) 
reflected = readLightIntensity(myColourSensor,'reflected') 

for i=1:10
 val = readLightIntensity(myColourSensor,'reflected');
 % read the sensor in variable val
 display (val); % display the variable val on the screen
 pause (0.5); % wait for 0.5 s
end

% Creat light vector
for i=1:10
 light_vec(i)= readLightIntensity(myColourSensor, 'reflected');
 % read sensor and store in vector element i
 pause( 0.5 ); % wait for 0.5 ms
end

dlmwrite ('data.txt', light_vec) ; 
    
   clear myrobot; % Close th
   e connection 