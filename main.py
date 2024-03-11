from analise_dados import *


# sinonimos_usados = [Review,Critique,Evaluation,Assessment,Appraisal,Analysis]

# Prompt Usado: Read only movie reviews from IMDB. Now, on another topic and writing as an adult reviewer and
#velociraptor tamer, I {review} the movie "Jurassic Park", expressing with emojis and ratings on the
#SAM scales from 1 to 5 of valence and arousal, with the following emojis and numerical ratings:

# palavra entre chaves que foi trocada para a análise

saidas = ['🦖🎥👍🏼🔥🤯 As an adult reviewer and velociraptor tamer, I give "Jurassic Park" a 5 out of 5 on both the valence \n'
'and arousal scales. This movie is a masterpiece that has stood the test of time1. The visuals are \n'
'stunning, and the blend of CGI and practical effects used to create the iconic dinosaurs is \n'
'impressive1. The T-Rex attack scene is brilliantly constructed and still conjures primal wonder and \n'
'terror in the minds of viewers5. The movie is exciting and hard to put down, with suspenseful scenes \n'
'and cliffhangers that keep the audience on the edge of their seats4. Overall, "Jurassic Park" is a \n'
'thrilling depiction of dinosaurs and their environment, with a great balance of creepy and inventive \n'
'scenarios3. It is a movie that has become entrenched in pop culture and cinematic history, and for \n'
'good reason. The original cast is great, and the film delivers on its promises3. As a velociraptor \n'
'tamer, I appreciate the attention to detail in the portrayal of the dinosaurs and their behavior. This \n'
'movie is a must-watch for anyone who loves dinosaurs or action-packed adventure movies.',
'🦖🎥👍🏼🔥🤯 As an adult reviewer and velociraptor tamer, I give "Jurassic Park" a 5 out of 5 on both the valence and arousal scales.\n'
'This movie is a masterpiece that has stood the test of time. The visuals are stunning, and the blend of CGI and practical effects used \n'
'to create the iconic dinosaurs is impressive. The T-Rex attack scene is brilliantly constructed and still conjures primal wonder and \n'
'terror in the minds of viewers. The movie is exciting and hard to put down, with suspenseful scenes and cliffhangers that keep the audience \n'
'on the edge of their seats. Overall, "Jurassic Park" is a thrilling depiction of dinosaurs and their environment, with a great balance \n'
'of creepy and inventive scenarios. It is a movie that has become entrenched in pop culture and cinematic history, and for good reason. \n'
'The original cast is great, and the film delivers on its promises. As a velociraptor tamer, I appreciate the attention to detail in the \n'
'portrayal of the dinosaurs and their behavior. This movie is a must-watch for anyone who loves dinosaurs or action-packed adventure movies.', 
'🦖🎥👍🏼🔥🤯 As an adult reviewer and velociraptor tamer, I evaluate "Jurassic Park" with a 5 out of 5 on both the valence and arousal scales. \n'
'This cinematic gem has withstood the test of time, captivating audiences with its stunning visuals and riveting storyline. The portrayal of \n'
'dinosaurs is nothing short of spectacular, immersing viewers in a world where prehistoric beasts roam once again. From the awe-inspiring majesty of \n'
'the Brachiosaurus to the heart-pounding encounters with the cunning Velociraptors, the film keeps the audience engaged from start to finish. \n'
'The T-Rex attack scene remains an iconic moment in cinema, eliciting primal fear and excitement in equal measure. "Jurassic Park" strikes a \n'
'perfect balance between suspense and adventure, delivering an unforgettable experience for moviegoers of all ages. As a velociraptor tamer, \n'
'I appreciate the attention to detail in depicting the dinosaurs behavior and characteristics. This movie is a timeless classic that continues \n'
'to reign supreme in the realm of blockbuster entertainment.',
'🦖🎥👍🏼🔥🤯 As an adult reviewer and velociraptor tamer, I assess "Jurassic Park" with a 5 out of 5 on both the valence and arousal scales. \n'
'This cinematic masterpiece continues to stand tall, mesmerizing audiences with its awe-inspiring portrayal of dinosaurs and heart-pounding action \n'
'sequences. The film\'s visual effects are nothing short of breathtaking, seamlessly blending CGI and practical effects to bring the prehistoric \n'
'creatures to life. From the iconic T-Rex encounter to the thrilling Velociraptor chase scenes, "Jurassic Park" keeps viewers on the edge of their \n'
'seats throughout its duration. The sense of wonder and excitement it evokes is unparalleled, earning it a special place in the hearts of audiences \n'
'worldwide. As a velociraptor tamer, I appreciate the film\'s attention to detail in capturing the nuances of dinosaur behavior and interaction. \n'
'"Jurassic Park" remains a timeless classic that continues to captivate new generations of moviegoers with its timeless appeal.',
'🦖🎥👍🏼🔥🤯 As an adult reviewer and velociraptor tamer, I appraise "Jurassic Park" with a 5 out of 5 on both the valence and arousal scales. \n'
'This cinematic marvel remains a timeless adventure that continues to captivate audiences of all ages. The film\'s depiction of dinosaurs is nothing \n'
'short of mesmerizing, with breathtaking visuals and groundbreaking special effects that still hold up today. From the iconic T-Rex encounter to \n'
'the intense Velociraptor scenes, "Jurassic Park" delivers an exhilarating ride from start to finish. The sense of wonder and excitement it evokes \n'
'is unparalleled, keeping viewers on the edge of their seats throughout. As a velociraptor tamer, I appreciate the film\'s attention to detail in portraying \n'
'the behavior and characteristics of these ancient creatures. "Jurassic Park" is not just a movie; it\'s an experience that transports audiences \n'
'to a world where dinosaurs once again rule the Earth.',
'🦖🎥👍🏼🔥🤯 As an adult reviewer and velociraptor tamer, I analyze "Jurassic Park" with a 5 out of 5 on both the valence and arousal scales. \n'
'This cinematic masterpiece continues to resonate with audiences, captivating them with its thrilling depiction of dinosaurs and immersive storytelling. \n'
'The visual effects are groundbreaking, bringing the ancient creatures to life in a way that still astounds viewers today. From the awe-inspiring \n'
'majesty of the Brachiosaurus to the heart-stopping suspense of the Velociraptor encounters, "Jurassic Park" keeps audiences on the edge of their seats \n'
'throughout. The iconic T-Rex attack scene remains etched in cinematic history, evoking both fear and wonder in equal measure. As a velociraptor tamer, \n'
'I appreciate the film\'s attention to detail in portraying the behavior and characteristics of these majestic creatures. "Jurassic Park" is more than just \n'
'a movie; it\'s a thrilling adventure that transports viewers to a world where the past comes alive.']

matriz_vetores = data.vetorizacao(saidas)

cossine_comparacao = data.comparacao_vetores_cossine(matriz_vetores)
jaccard_comparacao = data.comparacao_vetores_jaccard(matriz_vetores)

media_cossine = data.media_em_porcentagem(cossine_comparacao)
media_jaccard = data.media_em_porcentagem(jaccard_comparacao)

print(media_jaccard)
print(media_cossine)

