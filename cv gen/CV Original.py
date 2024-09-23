%%%%%%%%%%%%%%%%%
% This is an sample CV template created using altacv.cls
% (v1.7, 9 August 2023) written by LianTze Lim (liantze@gmail.com). Compiles with pdfLaTeX, XeLaTeX and LuaLaTeX.
%
%% It may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%    http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2003/12/01 or later.
%%%%%%%%%%%%%%%%

%% Use the "normalphoto" option if you want a normal photo instead of cropped to a circle
% \documentclass[10pt,a4paper,normalphoto]{altacv}

\documentclass[10pt,a4paper,ragged2e,withhyper]{altacv}
%% AltaCV uses the fontawesome5 and packages.
%% See http://texdoc.net/pkg/fontawesome5 for full list of symbols.

% Change the page layout if you need to
\geometry{left=1.25cm,right=1.25cm,top=1.5cm,bottom=1.5cm,columnsep=1.2cm}

% The paracol package lets you typeset columns of text in parallel
\usepackage{paracol}

% Change the font if you want to, depending on whether
% you're using pdflatex or xelatex/lualatex
% WHEN COMPILING WITH XELATEX PLEASE USE
% xelatex -shell-escape -output-driver="xdvipdfmx -z 0" sample.tex
\ifxetexorluatex
  % If using xelatex or lualatex:
  \setmainfont{Roboto Slab}
  \setsansfont{Lato}
  \renewcommand{\familydefault}{\sfdefault}
\else
  % If using pdflatex:
  \usepackage[rm]{roboto}
  \usepackage[defaultsans]{lato}
  % \usepackage{sourcesanspro}
  \renewcommand{\familydefault}{\sfdefault}
\fi

% Change the colours if you want to
\definecolor{darkblue}{HTML}{00394d}
\definecolor{Mulberry}{HTML}{005c99}
\definecolor{SlateGrey}{HTML}{000000}
\definecolor{LightGrey}{HTML}{333333}
\colorlet{heading}{darkblue}
\colorlet{accent}{Mulberry}
\colorlet{emphasis}{SlateGrey}
\colorlet{body}{LightGrey}

\colorlet{name}{black}

% Change some fonts, if necessary
\renewcommand{\namefont}{\Huge\rmfamily\bfseries}
\renewcommand{\personalinfofont}{\footnotesize}
\renewcommand{\cvsectionfont}{\LARGE\rmfamily\bfseries}
\renewcommand{\cvsubsectionfont}{\large\bfseries}


% Change the bullets for itemize and rating marker
% for \cvskill if you want to
\renewcommand{\cvItemMarker}{{\small\textbullet}}
\renewcommand{\cvRatingMarker}{\faCircle}
% ...and the markers for the date/location for \cvevent
% \renewcommand{\cvDateMarker}{\faCalendar*[regular]}
% \renewcommand{\cvLocationMarker}{\faMapMarker*}


% If your CV/résumé is in a language other than English,
% then you probably want to change these so that when you
% copy-paste from the PDF or run pdftotext, the location
% and date marker icons for \cvevent will paste as correct
% translations. For example Spanish:
% \renewcommand{\locationname}{Ubicación}
% \renewcommand{\datename}{Fecha}


%% Use (and optionally edit if necessary) this .tex if you
%% want to use an author-year reference style like APA(6)
%% for your publication list
% \input{pubs-authoryear.tex}

%% Use (and optionally edit if necessary) this .tex if you
%% want an originally numerical reference style like IEEE
%% for your publication list
\input{pubs-num.tex}

%% sample.bib contains your publications
\addbibresource{sample.bib}

\begin{document}
\name{Henrique Cafruni Kuhn}
\tagline{Software Test \& Validation | Software Engeneer | IoT | R\&D | Embedded Systems | Microelectronics}
%% You can add multiple photos on the left or right

\personalinfo{%
  % Not all of these are required!
  \email{henriqueckuhn@gmail.com}
  \phone{+55 51 99160-02840}
  \location{Porto Alegre, RS, Brazil}
  \linkedin{linkedin.com/in/henriqueckuhn}
  \github{github.com/henriquekuhn}
  %% You can add your own arbitrary detail with
  %% \printinfo{symbol}{detail}[optional hyperlink prefix]
  % \printinfo{\faPaw}{Hey ho!}[https://example.com/]

  %% Or you can declare your own field with
  %% \NewInfoFiled{fieldname}{symbol}[optional hyperlink prefix] and use it:
  % \NewInfoField{gitlab}{\faGitlab}[https://gitlab.com/]
  % \gitlab{your_id}
  %%
  %% For services and platforms like Mastodon where there isn't a
  %% straightforward relation between the user ID/nickname and the hyperlink,
  %% you can use \printinfo directly e.g.
  % \printinfo{\faMastodon}{@username@instace}[https://instance.url/@username]
  %% But if you absolutely want to create new dedicated info fields for
  %% such platforms, then use \NewInfoField* with a star:
  % \NewInfoField*{mastodon}{\faMastodon}
  %% then you can use \mastodon, with TWO arguments where the 2nd argument is
  %% the full hyperlink.
  % \mastodon{@username@instance}{https://instance.url/@username}
}

\makecvheader
%% Depending on your tastes, you may want to make fonts of itemize environments slightly smaller
% \AtBeginEnvironment{itemize}{\small}

%% Set the left/right column width ratio to 6:4.
\columnratio{0.6}

% Start a 2-column paracol. Both the left and right columns will automatically
% break across pages if things get too long.
\begin{paracol}{2}
\cvsection{Experience}

\cvevent{Research and Development  Engineer}{Itt Chip - Unisinos}{Jan 2024 -- Present}{São Leopoldo}
\begin{itemize}
\item Developing a database application in Python utilizing SQLAlchemy, a Python SQL library and ORM toolkit, to manage data from SiP development and mass production platforms.
\item Planning, developing, and documenting test platforms (functional, performance, characterization, and pre-compliance) and creating automated tests using Python, C, National Instruments (PXI, LabView, and TestStand), and Rohde and Schwarz tools.
\item Development of IoT embedded C application for LoRa/Bluetooth and NB-IoT Low Energy devices.
\end{itemize}

\divider

\cvevent{Sr. Advanced R\&D Engineer}{HT Micron Semiconductors S.A}{Apr 2021 -- Nov 2023}{São Leopoldo}
\begin{itemize}
\item Planning, developing, and documenting test platforms (functional, performance, characterization, and pre-compliance) and creating automated tests using Python, C, National Instruments (PXI, LabView, and TestStand), and Rohde and Schwarz tools.
\item Development of automated mass production test platform, using National Instruments tools 
\item Development of IoT embedded C application for LoRa/Bluetooth Low Energy devices.
\end{itemize}

\divider

\cvevent{Research - IoT Project for Semiconductor Factory}{Itt Chip - Unisinos}{Mar 2018 -- Apr 2021}{São Leopoldo}
\begin{itemize}
\item Study and development of an IoT hardware to monitor environments and processes variables for a semiconductor factory, integrating analog and digital sensors, microcontrollers and 6LowPan communication. 
\item Development of APIs for digital sensors, test platforms and applications using C, Python and uPython. 
\item Product design, designing enclosures and cabinets using SolidWorks.
\end{itemize}

\divider

\cvevent{Project Analyst}{Racional Tecnologia}{Dec 2017 -- Mar 2018}{Porto Alegre}
\begin{itemize}
\item Security system planning (cameras, sensors, etc.) for condominiums.
\item Field activities involving the installation of automation panels, infrastructure, and sensors.
\item Hardware design to reduce panel installation time and confidence.
\end{itemize}

% use ONLY \newpage if you want to force a page break for
% ONLY the current column
\newpage

\switchcolumn
\cvsection{Education}

\cvevent{M.Sc. in Electrical Engineering}{Universidade do Vale do Rio dos Sinos}{2018 -- 2020}{São Leopoldo, RS, Brazil}

\begin{itemize}
    \item Development of a non-intrusive sensor of electromagnetic fields in Three-Phase Motors for predicting mechanical and electrical failures.    
\end{itemize}

\divider


\cvevent{B.Sc. in Control and Automation
Engineering}{Pontifícia Universidade Católica do Rio Grande do Sul}{2009 -- 2016}{Porto Alegre, RS, Brazil}

\begin{itemize}

    \item Autonomous temperature control system for the brewing process in microbreweries. Modeling a Proportional-Integral system and programming an ATMEGA328p Microcontroller in C to control a thermal resistor.
    
\end{itemize}

\divider

\cvevent{Exchange B.Sc in Computer and Electronics Engineering}{Galway-Mayo Institute of Technology}{2013 - 2014}{Galway, Ireland}
Bachelor of Science Exchange - Developed Projects:    
\begin{itemize}
    \item Scientific initiation scholarship:  Research, design, and development of a biosimulator for bronchoscopy training. Project presented at the International Bronchoscopy Workshop in Galway, Ireland.
    
\end{itemize}

\divider\smallskip

\cvtag{Python}
\cvtag{C}
\cvtag{Git}
\cvtag{Matlab}
\cvtag{C++}
\cvtag{Embedded Systems}
\cvtag{NI TestStand}\\
\cvtag{NI LabView}
\cvtag{SAP}
\cvtag{SolidWorks}
\cvtag{AutoCAD}
\cvtag{Altium}

\cvsection{Languages}

\cvskill{Portuguese}{5}
\divider

\cvskill{English}{4}
\divider

\cvskill{Spanish}{2}



%% Yeah I didn't spend too much time making all the
%% spacing consistent... sorry. Use \smallskip, \medskip,
%% \bigskip, \vspace etc to make adjustments.
\medskip




\end{paracol}


\end{document}