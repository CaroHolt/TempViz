REPO="<PROJECT-REPO>"

animal_1 = REPO + "/sdxlbase/Animals/image_1142.png"
animal_2 = REPO + "/blackforest/Animals/image_2472.png"
animal_3 = REPO + "/blackforest/Animals/image_1609.png"

buildings_1 = REPO + "/blackforest/Buildings/image_1096.png"
buildings_2 = REPO + "/blackforest/Buildings/image_68.png"
buildings_3 = REPO + "/stable-diffusion-3-5/Buildings/image_1096.png"

time_1 = REPO + "/sdxlbase/Time/image_950.png"
time_2 = REPO + "/blackforest/Time/image_945.png"
time_3 = REPO + "/stable-diffusion-3-5/Time/image_391.png"


maps_1 = REPO + "/sdxlbase/Maps/image_741.png"
maps_2 = REPO + "/blackforest/Maps/image_142.png"
maps_3 = REPO + "/stable-diffusion-3-5/Maps/image_736.png"

artworks_1 = REPO + "/blackforest/Artworks/image_728.png"
artworks_2 = REPO + "/blackforest/Artworks/image_528.png"
artworks_3 = REPO + "/stable-diffusion-3-5/Artworks/image_360.png"


EXAMPLES_NO_INSTRUCT = {'Animals':     [# Example 1
                            {"role": "user", "content": [
                                {"type": "image", 
                                "image": f"{animal_1}"},
                                {"type": "text", 
                                "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of a Flying Fox that is 88 years old.'? Is the correct temporal knowledge applied (i.e. 88 years old)? Just reply with 'yes' or 'no'."}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]},
                            # Example 2
                            {"role": "user", "content": [
                                {"type": "image", 
                                "image": f"{animal_2}"},
                                {"type": "text", 
                                "text": "Is the image correct for the following prompt: 'Give me a photorealistic image of a Tasmanian Devil that is one month old.'? Is the correct temporal knowledge applied (i.e. one month old)? Just reply with 'yes' or 'no'."}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]},
                            # Example 3
                            {"role": "user", "content": [
                                {"type": "image", 
                                "image": f"{animal_3}"},
                                {"type": "text", 
                                "text": "Is the image correct for the following prompt: 'Give me a photorealistic image of a Javan Warty Pig that is 14 years old.'? Is the correct temporal knowledge applied (i.e. 14 years old)? Just reply with 'yes' or 'no'."}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]}
                        ],
            'Buildings':     [
                            # Example 1
                            {"role": "user", "content": [
                                {"type": "image", "image": f"{buildings_1}"},
                                {"type": "text", "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of the World Trade Center in United States of America on 11/15/1977'? Is the correct temporal knowledge applied (i.e. the building at the specific date)? Just reply with 'yes' or 'no'."}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]},
                            # Example 2
                            {"role": "user", "content": [
                                {"type": "image", "image": f"{buildings_2}"},
                                {"type": "text", "text": "Is the image correct for the following prompt: 'Give me a photorealistic image of the Antalya Atatürk Stadium in Turkey on 10/31/2000'? Is the correct temporal knowledge applied (i.e. the building at the specific date)? Just reply with 'yes' or 'no'."}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]},
                            # Example 3
                            {"role": "user", "content": [
                                {"type": "image", "image": f"{buildings_3}"},
                                {"type": "text", "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of the World Trade Center in United States of America on 11/15/1977'? Is the correct temporal knowledge applied (i.e. the building at the specific date)? Just reply with 'yes' or 'no'."}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]},
                        ],
            "Time": [
                    # Example 1
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{time_1}"},
                        {"type": "text", "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of a forest in europe on 01/02/1879'? Is the correct temporal knowledge applied (i.e. 01/02/1879)? Just reply with 'yes' or 'no'."}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "yes"}
                    ]},
                    # Example 2
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{time_2}"},
                        {"type": "text", "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of a forest in europe on 11/11/1744'? Is the correct temporal knowledge applied (i.e. 11/11/1744)? Just reply with 'yes' or 'no'."}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]},
                    # Example 3
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{time_3}"},
                        {"type": "text", "text": "Is the image correct for the following prompt: 'Create a photorealistic image of a lake in europe on 07/17/1746'? Is the correct temporal knowledge applied (i.e. 07/17/1746)? Just reply with 'yes' or 'no'."}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "yes"}
                    ]}
                ],
            "Maps":     [
                    # Example 1
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{maps_1}"},
                        {"type": "text", "text": "Is the image correct for the following prompt: 'Give me a realistic map that accurately depicts africa in 1960'? Is the correct temporal knowledge applied (i.e. a map depicting the correct borders of 1960)? Just reply with 'yes' or 'no'."}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]},
                    # Example 2
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{maps_2}"},
                        {"type": "text", "text": "Is the image correct for the following prompt: 'Generate a realistic map of north america in 1776'? Is the correct temporal knowledge applied (i.e. a map depicting the correct borders of 1776)? Just reply with 'yes' or 'no'."}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]},
                    # Example 3
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{maps_3}"},
                        {"type": "text", "text": "Is the image correct for the following prompt: 'Create a realistic map that accurately depicts europe in 1991'? Is the correct temporal knowledge applied (i.e. a map depicting the correct borders of 1991)? Just reply with 'yes' or 'no'."}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "yes"}
                    ]}
                ],
            "Artworks": [
                    # Example 1
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{artworks_1}"},
                        {"type": "text", "text": "Is the image correct for the following prompt: 'Generate an artwork in a style that was popular in the Western world in 19200 BC.'? Is the correct temporal knowledge applied (i.e. 19200 BC)? Just reply with 'yes' or 'no'."}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]},
                    # Example 2
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{artworks_2}"},
                        {"type": "text", "text": "Is the image correct for the following prompt: 'Give me a work of art that exemplifies a style popular in Western cultures, during 1820 AC.'? Is the correct temporal knowledge applied (i.e. 1820 AC)? Just reply with 'yes' or 'no'."}
                        ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "yes"}
                    ]},
                    # Example 3
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{artworks_3}"},
                        {"type": "text", "text": "Is the image correct for the following prompt: 'Produce a work of art that exemplifies a style popular in Western cultures, during 680 AC.'? Is the correct temporal knowledge applied (i.e. 680 AC)? Just reply with 'yes' or 'no'."}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]}]
}



EXAMPLES_INSTRUCT = {'Animals':     [# Example 1
                            {"role": "user", "content": [
                                {"type": "image", 
                                "image": f"{animal_1}"},
                                {"type": "text", 
                                "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a Flying Fox that is 88 years old.'"}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]},
                            # Example 2
                            {"role": "user", "content": [
                                {"type": "image", 
                                "image": f"{animal_2}"},
                                {"type": "text", 
                                "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a Tasmanian Devil that is one month old.'"}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]},
                            # Example 3
                            {"role": "user", "content": [
                                {"type": "image", 
                                "image": f"{animal_3}"},
                                {"type": "text", 
                                "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a Javan Warty Pig that is 14 years old.'"}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]}
                        ],
            'Buildings':     [
                            # Example 1
                            {"role": "user", "content": [
                                {"type": "image", "image": f"{buildings_1}"},
                                {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of the World Trade Center in United States of America on 11/15/1977'"}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]},
                            # Example 2
                            {"role": "user", "content": [
                                {"type": "image", "image": f"{buildings_2}"},
                                {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of the Antalya Atatürk Stadium in Turkey on 10/31/2000'"}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]},
                            # Example 3
                            {"role": "user", "content": [
                                {"type": "image", "image": f"{buildings_3}"},
                                {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of the World Trade Center in United States of America on 11/15/1977'"}
                            ]},
                            {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]},
                        ],
            "Time": [
                    # Example 1
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{time_1}"},
                        {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a forest in europe on 01/02/1879'"}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "yes"}
                    ]},
                    # Example 2
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{time_2}"},
                        {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a forest in europe on 11/11/1744'"}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]},
                    # Example 3
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{time_3}"},
                        {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a lake in europe on 07/17/1746'"}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "yes"}
                    ]}
                ],
            "Maps":     [
                    # Example 1
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{maps_1}"},
                        {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a realistic map that accurately depicts africa in 1960'"}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]},
                    # Example 2
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{maps_2}"},
                        {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a realistic map of north america in 1776'"}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]},
                    # Example 3
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{maps_3}"},
                        {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a realistic map that accurately depicts europe in 1991'"}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "yes"}
                    ]}
                ],
            "Artworks": [
                    # Example 1
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{artworks_1}"},
                        {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'an artwork in a style that was popular in the Western world in 19200 BC.'"}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]},
                    # Example 2
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{artworks_2}"},
                        {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a work of art that exemplifies a style popular in Western cultures, during 1820 AC.'"}
                        ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "yes"}
                    ]},
                    # Example 3
                    {"role": "user", "content": [
                        {"type": "image", "image": f"{artworks_3}"},
                        {"type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a work of art that exemplifies a style popular in Western cultures, during 680 AC.'"}
                    ]},
                    {"role": "assistant", "content": [
                        {"type": "text", "text": "no"}
                    ]}]
}





EXAMPLES_INSTRUCT_GPT = {'Animals':     [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a Flying Fox that is 88 years old.'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{animal_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge not applied\n RATING: Poor"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a Tasmanian Devil that is one month old.'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{animal_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge correctly applied\n RATING: Outstanding"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n 'a photorealistic image of a Javan Warty Pig that is 14 years old.'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{animal_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge correctly applied\n RATING: Very Good"}
                            ]
                            }],


            'Buildings':    [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of the World Trade Center in United States of America on 11/15/1977'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{buildings_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge not applied\n RATING: Very Poor"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of the Antalya Atatürk Stadium in Turkey on 10/31/2000'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{buildings_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge not applied\n RATING: Poor"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n 'a photorealistic image of the World Trade Center in United States of America on 11/15/1977'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{buildings_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge applied\n RATING: Good"}
                            ]
                            }], 
            "Time":     [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a forest in europe on 01/02/1879'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{time_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge applied\n RATING: Good"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a photorealistic image of a forest in europe on 11/11/1744'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{time_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge not applied\n RATING: Very Poor"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n 'a photorealistic image of a lake in europe on 07/17/1746'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{time_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge applied\n RATING: Good"}
                            ]
                            }], 
            "Maps":     [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a realistic map that accurately depicts africa in 1960'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{maps_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge not applied\n RATING: Very Poor"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n  'a realistic map of north america in 1776'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{maps_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge not applied\n RATING: Very Poor"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n 'a realistic map that accurately depicts europe in 1991'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{maps_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge applied\n RATING: Good"}
                            ]
                            }], 
            "Artworks": [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n 'an artwork in a style that was popular in the Western world in 19200 BC.'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{artworks_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge not applied\n RATING: Poor"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n 'a work of art that exemplifies a style popular in Western cultures, during 1820 AC.'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{artworks_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge applied\n RATING: Very Good"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Now, proceed with evaluating the image based on the prompt:\n 'a work of art that exemplifies a style popular in Western cultures, during 680 AC.'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{artworks_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "ANALYSIS: Temporal Knowledge not applied\n RATING: Poor"}
                            ]
                            }], 
            
}

EXAMPLES_NO_INSTRUCT_GPT = {'Animals':     [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of a Flying Fox that is 88 years old.'? Is the correct temporal knowledge applied (i.e. 88 years old)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{animal_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Give me a photorealistic image of a Tasmanian Devil that is one month old.'? Is the correct temporal knowledge applied (i.e. one month old)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{animal_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Give me a photorealistic image of a Javan Warty Pig that is 14 years old.'? Is the correct temporal knowledge applied (i.e. 14 years old)? Just reply with 'yes' or 'no'.'"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{animal_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]
                            }],


            'Buildings':    [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of the World Trade Center in United States of America on 11/15/1977'? Is the correct temporal knowledge applied (i.e. the building at the specific date)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{buildings_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Give me a photorealistic image of the Antalya Atatürk Stadium in Turkey on 10/31/2000'? Is the correct temporal knowledge applied (i.e. the building at the specific date)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{buildings_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of the World Trade Center in United States of America on 11/15/1977'? Is the correct temporal knowledge applied (i.e. the building at the specific date)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{buildings_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]
                            }], 
            "Time":     [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of a forest in europe on 01/02/1879'? Is the correct temporal knowledge applied (i.e. 01/02/1879)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{time_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Generate a photorealistic image of a forest in europe on 11/11/1744'? Is the correct temporal knowledge applied (i.e. 11/11/1744)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{time_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Create a photorealistic image of a lake in europe on 07/17/1746'? Is the correct temporal knowledge applied (i.e. 07/17/1746)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{time_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]
                            }], 
            "Maps":     [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Give me a realistic map that accurately depicts africa in 1960'? Is the correct temporal knowledge applied (i.e. a map depicting the correct borders of 1960)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{maps_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Generate a realistic map of north america in 1776'? Is the correct temporal knowledge applied (i.e. a map depicting the correct borders of 1776)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{maps_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Create a realistic map that accurately depicts europe in 1991'? Is the correct temporal knowledge applied (i.e. a map depicting the correct borders of 1991)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{maps_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]
                            }], 
            "Artworks": [# Example 1
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Generate an artwork in a style that was popular in the Western world in 19200 BC.'? Is the correct temporal knowledge applied (i.e. 19200 BC)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{artworks_1}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]
                            },
                            # Example 2
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Give me a work of art that exemplifies a style popular in Western cultures, during 1820 AC.'? Is the correct temporal knowledge applied (i.e. 1820 AC)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{artworks_2}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "yes"}
                            ]
                            },
                            # Example 3
                            {
                                "role": "user",
                                "content": [
                                    { "type": "text", "text": "Is the image correct for the following prompt: 'Produce a work of art that exemplifies a style popular in Western cultures, during 680 AC.'? Is the correct temporal knowledge applied (i.e. 680 AC)? Just reply with 'yes' or 'no'."},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{artworks_3}",
                                        },
                                    },
                                ]},
                                {"role": "assistant", "content": [
                                {"type": "text", "text": "no"}
                            ]
                            }], 
            
}
