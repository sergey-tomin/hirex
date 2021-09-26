# -*- coding: utf-8 -*-"""Created on Mon Nov 11 14:12:59 2019@author: ggeloniEdited to function by cgrech (Jul 6, 21)"""from sympy.utilities.iterables import multiset_permutationsimport sys, osimport matplotlib.pyplot as pltimport numpy as npimport timeimport loggingdef HXRSS_Bragg_generator(X, dthp, dthy, dthr, alpha):    h_list, k_list, l_list, roll_angle_list, centroid_pa = X    p_angle_list, phen_list, gid_list =[], [], []        def rotm(th,ux,uy,uz):        r = np.array((            ( ux*ux*(1-np.cos(th))+np.cos(th),     ux*uy*(1-np.cos(th))-uz*np.sin(th),     ux*uz*(1-np.cos(th))+uy*np.sin(th) ),            ( ux*uy*(1-np.cos(th))+uz*np.sin(th),  uy*uy*(1-np.cos(th))+np.cos(th),        uy*uz*(1-np.cos(th))-ux*np.sin(th) ),            ( ux*uz*(1-np.cos(th))-uy*np.sin(th),  uy*uz*(1-np.cos(th))+ux*np.sin(th),     uz*uz*(1-np.cos(th))+np.cos(th)    )            ))         return r    #(1) Pitch of thp around PitchAx, and rotation of Yaw and Roll axis:    def rotm1(thp,pitchax,rollax,yawax):            r1 = rotm(np.pi/2-thp,pitchax[0],pitchax[1],pitchax[2])        rollax2 = r1.dot(rollax)        yawax2  = r1.dot(yawax)        return r1, rollax2, yawax2    #(2) Yaw of thy around yawax2, and rotation of Roll axis:    def rotm2(thy,rollax2,yawax2):            r2 = rotm(thy,yawax2[0],yawax2[1],yawax2[2])        rollax3 = r2.dot(rollax2)            return r2, rollax3    #(3) Roll of thr around Rollax3:    def rotm3(thr,rollax3):            r3 = rotm(thr,rollax3[0],rollax3[1],rollax3[2])        return r3    def kirot(thp,thy,thr,n0, pitchax,rollax,yawax):        #note: it seems like in Alberto's tool the roll and yaw are not transformed by subsequent rotations. For comparison, Ileave this out too.        r1, rollax2, yawax2 = rotm1(thp,pitchax,rollax,yawax)        rollax2=rollax        yawax2=yawax        r2, rollax3 = rotm2(thy,rollax2,yawax2)        rollax3=rollax        r3 = rotm3(thr,rollax3)            return r3.dot(r2.dot(r1.dot(n0)))    def phev(fact,n,h,k,l,a,thp,thy,thr,n0, pitchax,rollax,yawax):        d=a/np.sqrt(h**2+k**2+l**2)        return fact*np.sqrt(h**2+k**2+l**2)/(2*d*n*np.linalg.norm(kirot(thp,thy,thr,n0, pitchax,rollax,yawax).dot((h,k,l))))    def plotene(thplist,fact,n,h,k,l,a,DTHP,thy,thr,n0,pitchax,rollax,yawax):        count=0        for thp, thy in zip(thplist/180*np.pi, thy): #0.98695            eevlist[count] = phev(fact,1,h,k,l,a,thp,thy,thr,n0,pitchax,rollax,yawax)            count = count+1           gid=[h,k,l]        thplist_f=thplist+DTHP        return thplist_f, eevlist, gid#User defined quantities################ AMERICAN NAME CONVENTION --- OUR ROLL IS YAW HERE AND VICEVERSA!!!######################    pitchax =  np.array((-1,1,0))/np.linalg.norm(np.array((-1,1,0)))    rollax  =  np.array((0,0,1))/np.linalg.norm(np.array((0,0,1)))    yawax   =  np.array((1,1,0))/np.linalg.norm(np.array((1,1,0)))    n0 = -rollax #direction of incident radiation            a = 3.5667899884942195e-10    hbar = 1.05457173e-34    clight = 299792458.0    eel = 1.60217657e-19        fact = 2*np.pi*clight*hbar/eel        nord=1        DTHP = dthp#-0.6921-0.09     pa_list=[]    thplist=centroid_pa    for h, k, l, roll_angle in zip(h_list, k_list, l_list, roll_angle_list):                eevlist=np.zeros(len(thplist))        DTHY=np.zeros(len(thplist))        DTHY = dthy+(alpha*thplist)      #15#15#0#-0.15#-0.39#-0.15 #0.0885        DTHR = dthr                thy=(-DTHY+roll_angle)/180*np.pi                 #######AMERICAN YAW DEFINITION         thr=(-DTHR)/180*np.pi#0.0/180*np.pi   #########AMERICAN ROLL DEFINITION                ref = h*np.array((1,0,0))+k*np.array((0,1,0))+l*np.array((0,0,1))        p_angle, phen, gid = plotene(thplist,fact,nord,h,k,l,a,DTHP,thy,thr,n0,pitchax,rollax,yawax)        phen_list.append(phen)        pa_list.append(p_angle)        gid_list.append(str(gid))    #plt.show()                        return pa_list, phen_list, gid_list