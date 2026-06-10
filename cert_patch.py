#!/usr/bin/env python3
"""Replace certificate section body (lines 935-1140) with new layout."""

with open('index.html', 'r') as f:
    lines = f.readlines()

# Card template helper
def card(img, title, pdf):
    return f'''            <div class="certificate-card group flex-shrink-0 w-[420px] h-[260px] bg-slate-800 rounded-2xl border border-white/5 shadow-xl flex justify-center items-center text-white transition-all duration-500 overflow-hidden bg-cover bg-center bg-no-repeat relative max-md:w-[280px] max-md:h-[175px]" style="background-image: url('{img}');">
              <div class="certificate-overlay absolute inset-0 bg-slate-950/75 backdrop-blur-[3px] flex flex-col justify-center items-center opacity-0 transition-all duration-300 p-6 text-center group-hover:opacity-100 max-md:opacity-100 max-md:bg-slate-950/60">
                <h3 class="text-white font-outfit font-black text-lg md:text-xl mb-3 tracking-tight">{title}</h3>
                <a href="{pdf}" target="_blank" class="view-pdf-btn inline-flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 text-white font-outfit font-bold py-2.5 px-6 rounded-xl transition-all duration-300 shadow-lg shadow-indigo-600/30 text-sm max-md:py-2 max-md:px-4">
                  <i class="far fa-file-pdf"></i> View PDF
                </a>
              </div>
            </div>
'''

# All certificates
all_certs = [
    ('./assets/certificate/certificate_dicoding_js.jpg', 'Basic JavaScript', './assets/certificate/certificate_dicoding_js.pdf'),
    ('./assets/certificate/certificate_dicoding_reactjs.jpg', 'Basic ReactJS', './assets/certificate/certificate_dicoding_reactjs.pdf'),
    ('./assets/certificate/certificate_dicoding_dasar_web.png', 'Basic Web Dev', './assets/certificate/certificate_dicoding_dasar_web.pdf'),
    ('./assets/certificate/certificate_pkl.jpg', 'Field Work Practice', './assets/certificate/certificate_pkl.pdf'),
    ('./assets/certificate/certificate_ai_dasar.png', 'Basic AI', './assets/certificate/certificate_ai_dasar.pdf'),
    ('./assets/certificate/certificate_dicoding-be.png', 'Basic Backend Dev', './assets/certificate/certificate_dicoding-be.pdf'),
    ('./assets/certificate/certificate_aws_cloud.png', 'Basic AWS Cloud', './assets/certificate/certificate_aws_cloud.pdf'),
    ('./assets/certificate/certificate_smk.jpg', 'Final Assignment', './assets/certificate/certificate_smk.pdf'),
    ('./assets/certificate/certificate_ai_generatif.png', 'Generative AI', './assets/certificate/certificate_ai_generatif.pdf'),
]

# Mobile Row 1: FE-focused
mobile_r1 = [all_certs[i] for i in [0,1,2,3,4]]  # JS, React, WebDev, PKL, AI
# Mobile Row 2: BE-focused
mobile_r2 = [all_certs[i] for i in [5,6,7,8]]  # BE, Cloud, SMK, AIGen

def make_cards(certs):
    return ''.join(card(*c) for c in certs)

def make_marquee_row(certs, direction, extra_class='', mb='mb-8'):
    anim = 'animate-marquee-left' if direction == 'left' else 'animate-marquee-right'
    cards_html = make_cards(certs)
    return f'''      <div class="marquee-container w-full overflow-hidden relative {mb} {extra_class}">
        <div class="marquee-track flex gap-8 py-2 w-max {anim} hover:[animation-play-state:paused] [will-change:transform]">
          <div class="flex gap-8 shrink-0">
{cards_html}          </div>
          <div class="flex gap-8 shrink-0" aria-hidden="true">
{cards_html}          </div>
        </div>
      </div>
'''

# Build new section body
new_body = ''

# Desktop: 1 row with all certs (hidden on mobile)
new_body += make_marquee_row(all_certs, 'left', extra_class='max-md:hidden', mb='')

# Mobile: 2 rows with different content (hidden on desktop)
new_body += make_marquee_row(mobile_r1, 'left', extra_class='hidden max-md:block', mb='mb-6')
new_body += make_marquee_row(mobile_r2, 'right', extra_class='hidden max-md:block', mb='')

new_body += '    </section>\n'

# Replace lines 935-1141 (0-indexed: 934-1140)
new_lines = lines[:934] + [new_body] + lines[1141:]

with open('index.html', 'w') as f:
    f.writelines(new_lines)

print("Done! Certificate section replaced.")
