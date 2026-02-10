import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

anime = ctk.CTk()
anime.geometry("700x500")
anime.title("Anime Tracker")

anime_label =ctk.CTkLabel(anime,
                          
                          text="Anime Tracker",

                           font=("Arial",30)
                           )
anime_label.pack(pady=10,)

anime_frame =ctk.CTkFrame(anime,
                            height=100, 
                              corner_radius=40)
anime_frame.pack(pady=5,fill ="x")

anime_name=ctk.CTkLabel(anime_frame,
                        
                         text="Enter The Name Of The Anime",

                           font =("Arial",13))
anime_name.pack(pady=15)

anime_entry=ctk.CTkEntry(anime_frame,
                          width=300, 
                          height=36, 
                          corner_radius=15)

anime_entry.pack(pady=5)

total_episode =ctk.CTkLabel(anime_frame,
                            text="Enter the Total number of Episode in The Anime",
                            font=("Arial",13))
total_episode.pack(pady=15)

total_anime_entry=ctk.CTkEntry(anime_frame, 
                               width=300,
                               height=36,
                                 corner_radius=15 )

total_anime_entry.pack(pady=5)

current_episode=ctk.CTkLabel(anime_frame, 
                             text="Enter your current episode",
                               font=("Arial", 13))

current_episode.pack(pady=15)

current_episode_entry=ctk.CTkEntry(anime_frame, 
                              width=300,
                                height=36, 
                                corner_radius=15)

current_episode_entry.pack(pady=5)

progress_bar=ctk.CTkProgressBar(anime_frame,
                                width=300)

progress_bar.set(0)
progress_bar.pack(pady=20)

def ani_loop():
    name = anime_entry.get()
    total_anime = total_anime_entry.get()
    current = current_episode_entry.get()

    if not total_anime.isdigit():
        anime_button.configure(text="Total anime must be a number")
        total_anime_entry.delete(0,"end")
        return

    if not current.isdigit():
        anime_button.configure(text="Current Episode must be a number")
        current_episode_entry.delete(0,"end")
        return
    
    total_anime = int(total_anime)
    current= int(current)

    if current > total_anime:
        anime_button.configure(text="Current Episode cannot be greater than the total anime")
        return
    
    progress = current /total_anime
    progress_bar.set(progress)

    remaning = total_anime - current

    anime_button.configure(text=f"You Are Currently Watching-- {name}. -- {current}/{total_anime} Episode Finished. {remaning} left.")

anime_button=ctk.CTkButton(anime, 
                           text="Click Me!",
                             command=ani_loop, 
                             corner_radius=15 )
anime_button.pack(pady=0)

def reset_button():
    anime_entry.delete(0,"end")
    total_anime_entry.delete(0,"end")
    current_episode_entry.delete(0,"end")
    anime_button.configure(text="Click Me!")

    progress_bar.set(0)
    
anime_reset=ctk.CTkButton(anime,
                          text="Reset",
                          corner_radius=15,
                          command=reset_button)

anime_reset.pack(pady=10, padx=100)

anime.mainloop()