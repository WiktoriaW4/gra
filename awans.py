def awans(self):
    print("Sprawdzasz możliwość awansu.")
    if self.policjant.umiejetnosci >= 15:
        print("Gratulacje! Otrzymałeś awans.")
        self.policjant.pieniadze += 2000
        self.policjant.zadowolenie_z_pracy += 20
        self.policjant.umiejetnosci = 0  
    else:
        print("Niestety, nie masz wystarczająco umiejętności, aby otrzymać awans.")
        print(f"Twoje umiejętności: {self.policjant.umiejetnosci}/15")